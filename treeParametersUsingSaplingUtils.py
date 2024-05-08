import bpy
import importlib
import os
import ast
import operator
import numpy as np
import pprint
import time
import re
import sys

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

from random import random, uniform, seed, choice, getstate, setstate, randint
from math import pi
import createTree as us

tau = 2 * pi


class TreeParametersUsingSaplingUtils(object):
    @property
    def bevel(self):
        return self._bevel

    @bevel.setter
    def bevel(self, val):
        self._bevel = val

    @property
    def prune(self):
        return self._prune

    @prune.setter
    def prune(self, val):
        self._prune = val

    @property
    def showLeaves(self):
        return self._showLeaves

    @showLeaves.setter
    def showLeaves(self, val):
        self._showLeaves = val

    @property
    def useArm(self):
        return self._useArm

    @useArm.setter
    def useArm(self, val):
        self._useArm = val

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, val):
        self._seed = val

    @property
    def handleType(self):
        return self._handleType

    @handleType.setter
    def handleType(self, val):
        if val == '0' or val == '1':
            self._handleType = val
        else:
            self._handleType = '0'

    @property
    def levels(self):
        return self._levels

    @levels.setter
    def levels(self, val):
        if 1 <= val <= 4:
            self._levels = int(val)
        else:
            self._levels = 1

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, val):
        index = 0
        for v in val:
            if v >= 0.000001:
                self._length[index] = v
            else:
                self._length[index] = 0.000001
            index = index + 1

    @property
    def lengthV(self):
        return self._lengthV

    @lengthV.setter
    def lengthV(self, val):
        index = 0
        for v in val:
            if v >= 0.0 and v <= 1.0:
                self._lengthV[index] = v
            else:
                self._lengthV[index] = 0.0
            index = index + 1

    @property
    def taperCrown(self):
        return self._taperCrown

    @taperCrown.setter
    def taperCrown(self, val):
        if val >= 0.0 and val <= 1.0:
            self._taperCrown = val
        else:
            self._taperCrown = 0.0

    @property
    def branches(self):
        return self._branches

    @branches.setter
    def branches(self, val):
        index = 0
        for v in val:
            if v >= 0.0:
                self._branches[index] = int(v)
            else:
                self._branches[index] = 0.0
            index = index + 1

    @property
    def curveRes(self):
        return self._curveRes

    @curveRes.setter
    def curveRes(self, val):
        index = 0
        for v in val:
            if v >= 1:
                self._curveRes[index] = int(v)
            else:
                self._curveRes[index] = 1
            index = index + 1

    @property
    def curve(self):
        return self._curve

    @curve.setter
    def curve(self, val):
        self._curve = list(val)

    @property
    def curveV1(self):
        return self._curveV1

    @curveV1.setter
    def curveV1(self, val):
        self._curveV1 = val

    @property
    def curveV2(self):
        return self._curveV2

    @curveV2.setter
    def curveV2(self, val):
        self._curveV2 = val

    @property
    def curveBack(self):
        return self._curveBack

    @curveBack.setter
    def curveBack(self, val):
        self._curveBack = list(val)

    @property
    def baseSplits(self):
        return self._baseSplits

    @baseSplits.setter
    def baseSplits(self, val):
        if val >= 0:
            self._baseSplits = int(val)
        else:
            self._baseSplits = 0

    @property
    def maxBaseSplits(self):
        return self._maxBaseSplits

    @maxBaseSplits.setter
    def maxBaseSplits(self, val):
        if val >= 0:
            self._maxBaseSplits = int(val)
        else:
            self._maxBaseSplits = 0

    @property
    def segSplits(self):
        return self._segSplits

    @segSplits.setter
    def segSplits(self, val):
        index = 0
        for v in val:
            if v >= 0.0 and v <= 3.0:
                self._segSplits[index] = v
            else:
                self._segSplits[index] = 0.0
            index = index + 1

    @property
    def splitByLen(self):
        return self._splitByLen

    @splitByLen.setter
    def splitByLen(self, val):
        self._splitByLen = val

    @property
    def rMode(self):
        return self._rMode

    @rMode.setter
    def rMode(self, val):
        if val == 'original' or val == 'rotate':
            self._rMode = val
        else:
            self._rMode = 'rotate'

    @property
    def splitAngle(self):
        return self._splitAngle

    @splitAngle.setter
    def splitAngle(self, val):
        self._splitAngle = list(val)

    @property
    def splitAngleV1(self):
        return self._splitAngleV1

    @splitAngleV1.setter
    def splitAngleV1(self, val):
        self._splitAngleV1 = val

    @property
    def splitAngleV2(self):
        return self._splitAngleV2

    @splitAngleV2.setter
    def splitAngleV2(self, val):
        self._splitAngleV2 = val

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, val):
        if val >= 0.0:
            self._scale = val
        else:
            self._scale = 1.0

    @property
    def scaleV(self):
        return self._scaleV

    @scaleV.setter
    def scaleV(self, val):
        self._scaleV = val

    @property
    def attractUp(self):
        return self._attractUp

    @attractUp.setter
    def attractUp(self, val):
        self._attractUp = list(val)

    @property
    def attractOut(self):
        return self._attractOut

    @attractOut.setter
    def attractOut(self, val):
        index = 0
        for v in val:
            if v >= 0.0 and v <= 1.0:
                self._attractOut[index] = v
            else:
                self._attractOut[index] = 0.0
            index = index + 1

    shapeList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '10']

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, val):
        if val in self.shapeList:
            self._shape = val
        else:
            self._shape = self.shapeList[0]

    shapeSList = ['0', '1', '2', '3', '4', '5', '6', '7', '10']

    @property
    def shapeS(self):
        return self._shapeS

    @shapeS.setter
    def shapeS(self, val):
        if val in self.shapeSList:
            self._shapeS = val
        else:
            self._shapeS = self.shapeSList[0]

    @property
    def customShape(self):
        return self._customShape

    @customShape.setter
    def customShape(self, val):
        index = 0
        for v in val:
            if v >= 0.01 and v <= 1.0:
                self._customShape[index] = v
            else:
                self._customShape[index] = 0.01
            index = index + 1

    @property
    def branchDist(self):
        return self._branchDist

    @branchDist.setter
    def branchDist(self, val):
        if val >= 0.1 and val <= 10.0:
            self._branchDist = val
        else:
            self._branchDist = 0.1

    @property
    def nrings(self):
        return self._nrings

    @nrings.setter
    def nrings(self, val):
        if val >= 0:
            self._nrings = int(val)
        else:
            self._nrings = 0

    @property
    def baseSize(self):
        return self._baseSize

    @baseSize.setter
    def baseSize(self, val):
        if val >= 0.0 and val <= 1.0:
            self._baseSize = val
        else:
            self._baseSize = 0.0

    @property
    def baseSize_s(self):
        return self._baseSize_s

    @baseSize_s.setter
    def baseSize_s(self, val):
        if val >= 0.0 and val <= 1.0:
            self._baseSize_s = val
        else:
            self._baseSize_s = 0.0

    @property
    def splitHeight(self):
        return self._splitHeight

    @splitHeight.setter
    def splitHeight(self, val):
        if val >= 0.0 and val <= 1.0:
            self._splitHeight = val
        else:
            self._splitHeight = 0.0

    @property
    def splitBias(self):
        return self._splitBias

    @splitBias.setter
    def splitBias(self, val):
        if val >= -2.0 and val <= 2.0:
            self._splitBias = val
        else:
            self._splitBias = 0.0

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, val):
        if val >= 0.0:
            self._ratio = val
        else:
            self._ratio = 0.0

    @property
    def minRadius(self):
        return self._minRadius

    @minRadius.setter
    def minRadius(self, val):
        if val >= 0.0:
            self._minRadius = val
        else:
            self._minRadius = 0.0

    @property
    def closeTip(self):
        return self._closeTip

    @closeTip.setter
    def closeTip(self, val):
        self._closeTip = val

    @property
    def rootFlare(self):
        return self._rootFlare

    @rootFlare.setter
    def rootFlare(self, val):
        if val >= 1.0:
            self._rootFlare = val
        else:
            self._rootFlare = 1.0

    @property
    def autoTaper(self):
        return self._autoTaper

    @autoTaper.setter
    def autoTaper(self, val):
        self._autoTaper = val

    @property
    def taper(self):
        return self._taper

    @taper.setter
    def taper(self, val):
        index = 0
        for v in val:
            if v >= 0.0 and v <= 1.0:
                self._taper[index] = v
            else:
                self._taper[index] = 1.0
            index = index + 1

    @property
    def radiusTweak(self):
        return self._radiusTweak

    @radiusTweak.setter
    def radiusTweak(self, val):
        index = 0
        for v in val:
            if v >= 0.0 and v <= 1.0:
                self._radiusTweak[index] = v
            else:
                self._radiusTweak[index] = 1.0
            index = index + 1

    @property
    def ratioPower(self):
        return self._ratioPower

    @ratioPower.setter
    def ratioPower(self, val):
        if val >= 0.0:
            self._ratioPower = val
        else:
            self._ratioPower = 0.0

    @property
    def downAngle(self):
        return self._downAngle

    @downAngle.setter
    def downAngle(self, val):
        self._downAngle = list(val)

    @property
    def downAngleV(self):
        return self._downAngleV

    @downAngleV.setter
    def downAngleV(self, val):
        self._downAngleV = list(val)

    @property
    def useOldDownAngle(self):
        return self._useOldDownAngle

    @useOldDownAngle.setter
    def useOldDownAngle(self, val):
        self._useOldDownAngle = val

    @property
    def useParentAngle(self):
        return self._useParentAngle

    @useParentAngle.setter
    def useParentAngle(self, val):
        self._useParentAngle = val

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, val):
        self._rotate = list(val)

    @property
    def rotateV(self):
        return self._rotateV

    @rotateV.setter
    def rotateV(self, val):
        self._rotateV = list(val)

    @property
    def scale0(self):
        return self._scale0

    @scale0.setter
    def scale0(self, val):
        if val >= 0.0:
            self._scale0 = val
        else:
            self._scale0 = 1.0

    @property
    def scaleV0(self):
        return self._scaleV0

    @scaleV0.setter
    def scaleV0(self, val):
        if val >= 0.0 and val <= 0.9:
            self._scaleV0 = val
        else:
            self._scaleV0 = 0.0

    @property
    def pruneWidth(self):
        return self._pruneWidth

    @pruneWidth.setter
    def pruneWidth(self, val):
        if val >= 0.0:
            self._pruneWidth = val
        else:
            self._pruneWidth = 0.0

    @property
    def pruneBase(self):
        return self._pruneBase

    @pruneBase.setter
    def pruneBase(self, val):
        if val >= 0.0 and val < 1.0:
            self._pruneBase = val
        else:
            self._pruneBase = 0.0

    @property
    def pruneWidthPeak(self):
        return self._pruneWidthPeak

    @pruneWidthPeak.setter
    def pruneWidthPeak(self, val):
        if val >= 0.0:
            self._pruneWidthPeak = val
        else:
            self._pruneWidthPeak = 0.0

    @property
    def prunePowerHigh(self):
        return self._prunePowerHigh

    @prunePowerHigh.setter
    def prunePowerHigh(self, val):
        self._prunePowerHigh = val

    @property
    def prunePowerLow(self):
        return self._prunePowerLow

    @prunePowerLow.setter
    def prunePowerLow(self, val):
        self._prunePowerLow = val

    @property
    def pruneRatio(self):
        return self._pruneRatio

    @pruneRatio.setter
    def pruneRatio(self, val):
        if val >= 0.0 and val < 1.0:
            self._pruneRatio = val
        else:
            self._pruneRatio = 0.0

    @property
    def leaves(self):
        return self._leaves

    @leaves.setter
    def leaves(self, val):
        self._leaves = int(val)

    @property
    def leafDownAngle(self):
        return self._leafDownAngle

    @leafDownAngle.setter
    def leafDownAngle(self, val):
        self._leafDownAngle = val

    @property
    def leafDownAngleV(self):
        return self._leafDownAngleV

    @leafDownAngleV.setter
    def leafDownAngleV(self, val):
        self._leafDownAngleV = val

    @property
    def leafRotate(self):
        return self._leafRotate

    @leafRotate.setter
    def leafRotate(self, val):
        self._leafRotate = val

    @property
    def leafRotateV(self):
        return self._leafRotateV

    @leafRotateV.setter
    def leafRotateV(self, val):
        self._leafRotateV = val

    @property
    def leafScale(self):
        return self._leafScale

    @leafScale.setter
    def leafScale(self, val):
        if val >= 0.0:
            self._leafScale = val
        else:
            self._leafScale = 1.0

    @property
    def leafScaleX(self):
        return self._leafScaleX

    @leafScaleX.setter
    def leafScaleX(self, val):
        if val >= 0.0:
            self._leafScaleX = val
        else:
            self._leafScaleX = 0.0

    @property
    def leafScaleT(self):
        return self._leafScaleT

    @leafScaleT.setter
    def leafScaleT(self, val):
        if val >= -1.0 and val <= 1.0:
            self._leafScaleT = val
        else:
            self._leafScaleT = 0.0

    @property
    def leafScaleV(self):
        return self._leafScaleV

    @leafScaleV.setter
    def leafScaleV(self, val):
        if val >= 0.0 and val <= 0.9:
            self._leafScaleV = val
        else:
            self._leafScaleV = 0.1

    leafShapeList = ['hex', 'rect', 'dFace', 'dVert']

    @property
    def leafShape(self):
        return self._leafShape

    @leafShape.setter
    def leafShape(self, val):
        if val in self.leafShapeList:
            self._leafShape = val
        else:
            self._leafShape = self.leafShapeList[1]

    @property
    def leafDupliObj(self):
        return self._leafDupliObj

    @leafDupliObj.setter
    def leafDupliObj(self, val):
        self._leafDupliObj = val

    @property
    def bend(self):
        return self._bend

    @bend.setter
    def bend(self, val):
        self._bend = val

    @property
    def leafangle(self):
        return self._leafangle

    @leafangle.setter
    def leafangle(self, val):
        self._leafangle = val

    @property
    def horzLeaves(self):
        return self._horzLeaves

    @horzLeaves.setter
    def horzLeaves(self, val):
        self._horzLeaves = val

    leafDistList = ['0', '1', '2', '3', '4', '5', '6', '7', '10']

    @property
    def leafDist(self):
        return self._leafDist

    @leafDist.setter
    def leafDist(self, val):
        if val in self.leafDistList:
            self._leafDist = val
        else:
            self._leafDist = self.leafDistList[0]

    @property
    def bevelRes(self):
        return self._bevelRes

    @bevelRes.setter
    def bevelRes(self, val):
        if val >= 0 and val <= 32:
            self._bevelRes = int(val)
        else:
            self._bevelRes = 0

    @property
    def resU(self):
        return self._resU

    @resU.setter
    def resU(self, val):
        if val >= 1:
            self._resU = int(val)
        else:
            self._resU = 1

    @property
    def armAnim(self):
        return self._armAnim

    @armAnim.setter
    def armAnim(self, val):
        self._armAnim = val

    @property
    def previewArm(self):
        return self._previewArm

    @previewArm.setter
    def previewArm(self, val):
        self._previewArm = val

    @property
    def leafAnim(self):
        return self._leafAnim

    @leafAnim.setter
    def leafAnim(self, val):
        self._leafAnim = val

    @property
    def frameRate(self):
        return self._frameRate

    @frameRate.setter
    def frameRate(self, val):
        if val >= 0.001:
            self._frameRate = val
        else:
            self._frameRate = 0.001

    @property
    def loopFrames(self):
        return self._loopFrames

    @loopFrames.setter
    def loopFrames(self, val):
        if val >= 0:
            self._loopFrames = int(val)
        else:
            self._loopFrames = 0

    @property
    def wind(self):
        return self._wind

    @wind.setter
    def wind(self, val):
        self._wind = val

    @property
    def gust(self):
        return self._gust

    @gust.setter
    def gust(self, val):
        self._gust = val

    @property
    def gustF(self):
        return self._gustF

    @gustF.setter
    def gustF(self, val):
        self._gustF = val

    @property
    def af1(self):
        return self._af1

    @af1.setter
    def af1(self, val):
        self._af1 = val

    @property
    def af2(self):
        return self._af2

    @af2.setter
    def af2(self, val):
        self._af2 = val

    @property
    def af3(self):
        return self._af3

    @af3.setter
    def af3(self, val):
        self._af3 = val

    @property
    def af4(self):
        return self._af4

    @af4.setter
    def af4(self, val):
        self._af4 = val

    @property
    def makeMesh(self):
        return self._makeMesh

    @makeMesh.setter
    def makeMesh(self, val):
        self._makeMesh = val

    @property
    def armLevels(self):
        return self._armLevels

    @armLevels.setter
    def armLevels(self, val):
        if val >= 0:
            self._armLevels = int(val)
        else:
            self._armLevels = 0

    @property
    def boneStep(self):
        return self._boneStep

    @boneStep.setter
    def boneStep(self, val):
        index = 0
        for v in val:
            if v >= 1:
                self._boneStep[index] = int(v)
            else:
                self._boneStep[index] = 1
            index = index + 1

    @property
    def rSplits2(self):
        return self._rSplits2

    @rSplits2.setter
    def rSplits2(self, val):
        self._rSplits2 = val

    @property
    def choiceNegPos1(self):
        return self._choiceNegPos1

    @choiceNegPos1.setter
    def choiceNegPos1(self, val):
        self._choiceNegPos1 = val

    @property
    def choiceNegPos2(self):
        return self._choiceNegPos2

    @choiceNegPos2.setter
    def choiceNegPos2(self, val):
        self._choiceNegPos2 = val

    @property
    def randTau1(self):
        return self._randTau1

    @randTau1.setter
    def randTau1(self, val):
        self._randTau1 = val

    @property
    def randTau2(self):
        return self._randTau2

    @randTau2.setter
    def randTau2(self, val):
        self._randTau2 = val

    @property
    def rLastAng(self):
        return self._rLastAng

    @rLastAng.setter
    def rLastAng(self, val):
        self._rLastAng = val

    @property
    def num_tree(self):
        return self._num_tree

    @num_tree.setter
    def num_tree(self, val):
        self._num_tree = val

    def __init__(self, _filename='', _variateCurve=False, output_path=''):
        self.variateCurve = _variateCurve
        self.filename = _filename
        self.output_path = output_path
        # self.folder = _folder
        self._num_tree = -1
        self._bevel = True
        self._prune = False
        self._showLeaves = True
        self._useArm = False
        self._seed = 0
        self._handleType = '0'  # tra 0 e 1
        self._levels = 3  # tra 1 e 4
        self._length = [1, 0.3, 0.6, 0.45]  # 0.000001
        self._lengthV = [0.0, 0.0, 0.0, 0.0]  # tra 0.0 e 1.0
        self._taperCrown = 0.0  # tra 0.0 e 1.0
        self._branches = [50, 30, 10, 10]  # min 0
        self._curveRes = [3, 5, 3, 1]  # min 1
        self._curve = [0.0, -40 - 0, -40.0, 0.0]
        self._curveV1 = [20.0, 50.0, 75.0, 0.0]
        self._curveV2 = [20.0, 50.0, 75.0, 0.0]
        self._curveBack = [0.0, 0.0, 0.0, 0.0]
        self._baseSplits = 0  # min 0
        self._maxBaseSplits = 0  # min 0
        self._segSplits = [0.0, 0.0, 0.0, 0.0]  # tra 0 e 3
        self._splitByLen = True
        self._rMode = "rotate"
        self._splitAngle = [0.0, 0.0, 0.0, 0.0]
        self._splitAngleV1 = [0, 0, 0, 0]
        self._splitAngleV2 = [0, 0, 0, 0]
        self._scale = 13.0  # min 0
        self._scaleV = 3.0
        self._attractUp = [0.0, 0.0, 0.0, 0.0]
        self._attractOut = [0.0, 0.0, 0.0, 0.0]  # tra 0.0 e 1.0
        self._shape = '7'
        self._shapeS = '4'
        self._customShape = [.5, 1.0, .3, .5]  # tra 0.01 e 1
        self._branchDist = 1.0  # tra 0.1 e 10
        self._nrings = 0  # min 0
        self._baseSize = 0.4  # tra 0.0 e 1.0
        self._baseSize_s = 0.25  # tra 0.0 e 1.0
        self._splitHeight = 0.2  # tra 0.0 e 1.0
        self._splitBias = 0.0  # tra -2.0 e 2.0
        self._ratio = 0.015  # min 0.0
        self._minRadius = 0.0  # min 0.0
        self._closeTip = False
        self._rootFlare = 1.0  # min 1.0
        self._autoTaper = False
        self._taper = [1, 1, 1, 1]  # tra 0.0 e 1.0
        self._radiusTweak = [1, 1, 1, 1]  # tra 0.0 e 1.0
        self._ratioPower = 1.2  # min 0.0
        self._downAngle = [90.0, 60.0, 45.0, 45.0]
        self._useOldDownAngle = False
        self._downAngleV = [0.0, 50.0, 10.0, 10.0]
        self._useParentAngle = False
        self._rotate = [137.5, 137.5, 137.5, 137.5]
        self._rotateV = [0.0, 0.0, 0.0, 0.0]
        self._scale0 = 1.0  # min 0.0
        self._scaleV0 = 0.2  # tra 0.0 e 1.0
        self._pruneWidth = 0.4  # min 0.0
        self._pruneBase = 0.3  # tra 0.0 e 1.0
        self._pruneWidthPeak = 0.6  # min 0.0
        self._prunePowerHigh = 0.5
        self._prunePowerLow = 0.001
        self._pruneRatio = 1.0  # tra 0.0 e 1.0
        self._leaves = 25
        self._leafDownAngle = 45.0
        self._leafDownAngleV = 10.0
        self._leafRotate = 137.5
        self._leafRotateV = 0.0
        self._leafScale = 0.17  # min 0.0
        self._leafScaleX = 1.0  # min 0.0
        self._leafScaleT = 0.0  # tra -1.0 e 1.0
        self._leafScaleV = 0.0  # tra 0.0 e 1.0
        self._leafShape = 'rect'
        self._leafDupliObj = False
        self._bend = 0
        self._leafangle = 0.0
        self._horzLeaves = True
        self._leafDist = '6'
        self._bevelRes = 0  # tra 0 e 32
        self._resU = 4  # min 1
        self._armAnim = False
        self._previewArm = False
        self._leafAnim = False
        self._frameRate = 1  # min 0.001
        self._armLevels = 2  # min 0
        self._loopFrames = 0  # min 0
        self._wind = 1.0
        self._gust = 1.0
        self._gustF = 0.075
        self._af1 = 1.0
        self._af2 = 1.0
        self._af3 = 4.0
        self._af4 = 4.0
        self._makeMesh = False
        self._boneStep = [1, 1, 1, 1]  # min 1
        self._rSplits2 = 0
        self._choiceNegPos1 = -1
        self._choiceNegPos2 = -1
        self._randTau1 = tau
        self._randTau2 = tau
        self._rLastAng = [0, 0, 0, 0]

    def importDataFromDir(self, filename):
        # Make sure the operator knows about the global variables
        # global settings, useSet
        # Read the preset data into the global settings
        settings = {}
        # try:
        # f = open(filename, 'r')
        # settings_str = f.readline()
        # f.close()
        # print(settings)
        # settings = ast.literal_eval(settings_str)

        file = open(filename, "r")
        contents = file.read()

        settings = ast.literal_eval(contents)
        file.close()

        # use old attractup
        if type(settings['attractUp']) == float:
            atr = settings['attractUp']
            settings['attractUp'] = [0, 0, atr, atr]

        # use old leaf rotations
        if 'leafDownAngle' not in settings:
            l = settings['levels']
            settings['leafDownAngle'] = settings['downAngle'][min(l, 3)]
            settings['leafDownAngleV'] = settings['downAngleV'][min(l, 3)]
            settings['leafRotate'] = settings['rotate'][min(l, 3)]
            settings['leafRotateV'] = settings['rotateV'][min(l, 3)]

        # zero leaf bend
        settings['bend'] = 0
            # print(settings)

            # Set the flag to use the settings
            # useSet = True
        # except (FileNotFoundError, IOError):
        #     print("File Not Found")
            # f = open(os.path.join(getPresetpaths()[1], self.filename), 'r')
        return settings

    def load_tree(self, load_and_save=True):
        print("loading ", "...", sep=self.filename)
        index_of_underscore = self.filename.find('_')
        substr = self.filename[:index_of_underscore]
        if substr.isnumeric():
            self.num_tree = int(substr)
        dirname = os.path.dirname(__file__)
        name = self.filename

        print("dirname: ", dirname)
        path = name
        print(path)

        settings = self.importDataFromDir(path)

        if len(settings) != 0:
            for a, b in settings.items():
                setattr(self, a, b)

        seed(self.seed)
        # for item in vars(self).items():
        #     if isinstance(item, tuple):
        #         item = list(item)

        # self.handleType = '1'
        # print(self.handleType)
        # print("splitAngleV: ", self.splitAngleV)
        if load_and_save is False:
            self._leafScaleV = settings['leafScaleV']
            self._scaleV0 = settings['scaleV0']

            # attrs = vars(self)
            # print(', '.join("%s: %s" % item for item in attrs.items()))

        # except Exception as err:
        #     print(err)
        #     print("Tree named ", " not exists", sep = self.filename)

    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        '''
        alist.sort(key=natural_keys) sorts in human order
        http://nedbatchelder.com/blog/200712/human_sorting.html
        (See Toothy's implementation in the comments)
        '''
        return [self.atoi(c) for c in re.split(r'(\d+)', text)]

    def select_name(self, tree_name, path, count=0):
        # folder = os.listdir(path)
        # full_name = str(len(folder) - 1) + "_" + tree_name + ".py"
        folder = os.listdir(path)
        folder.sort(key=self.natural_keys)
        # print(folder)
        n_images = len(folder)
        # n_images = dim_folder-1
        if n_images < 1:
            count = 0
        else:
            last_img_name = folder[-1]
            # print("last_image_name: ", last_img_name)
            index_of_underscore = last_img_name.find('_')
            if index_of_underscore == -1:
                count = 0
            else:
                last_image_number = int(last_img_name[:index_of_underscore])
                count = last_image_number + 1
        self.num_tree = count
        full_name = str(count) + "_" + tree_name + ".py"
        # full_name = str(count) + "_" + tree_name + ".py"
        # for file in os.listdir(path):
        #     if file == full_name:
        #         full_name = self.select_name(tree_name, path, count + 1)
        return full_name

    def dict_without_underscores(self):
        variables = self.__dict__.keys()
        values = self.__dict__.values()
        new_variables = [v.replace('_', '', 1) for v in variables]
        # print(new_variables)
        d = dict(zip(new_variables, values))
        # print(d)
        return d

    def exclude_dict(self, d, keys):
        return {x: d[x] for x in d if x not in keys}

    def save_tree(self):
        dirname = os.path.dirname(__file__)
        # path = os.path.join(dirname, "tree_params_sapling")
        path2 = os.path.join(dirname, "tree")
        # full_name = self.select_name(self.filename, path)
        full_name2 = self.select_name(self.filename, path2)
        print("saving ", "...", sep=full_name2)
        # path = os.path.join(path, full_name)
        path2 = os.path.join(path2, full_name2)
        dictionary = self.dict_without_underscores()
        # print(dictionary)
        keys = ['variateCurve', 'filename', 'num_tree', 'folder', 'bevel', 'showLeaves',
                'useArm', 'handleType', 'splitByLen', 'rMode',
                'closeTip', 'autoTaper',
                ''' 'useOldDownAngle', 'useParentAngle', 
                'prune', 'pruneWidth', 'prunebase',
                'pruneWidthPeak', 'prunePowerHigh', 
                'prunePowerLow', 'pruneRatio', '''
                'leafShape', 'leafDupliObj', 'bend',
                'armAnim', 'previewArm', 'leafAnim', 'frameRate',
                'armLevels', 'loopFrames', 'wind', 'gust', 'gustF',
                'af1', 'af2', 'af3', 'af4', 'makeMesh', 'boneStep',
                'randTau1', 'randTau2', 'splitAngleV', 'curveV']

        dictionary_variable = self.exclude_dict(dictionary, keys)
        # dictionary_variable = dictionary
        # f = open(path,"w")
        # # f.write( str(dictionary) )
        # f.write(pprint.pformat(dictionary))
        # f.close()

        f2 = open(path2, "w")
        # f.write( str(dictionary) )
        f2.write(pprint.pformat(dictionary_variable))
        f2.close()

    def choose_uniform_mode(self, val1, val2, mode):
        if mode == 1:
            return uniform(-val1, val2)
        if mode == 2:
            return uniform(1 - val1, 1 + val2)
        if mode == 3:
            # return uniform(min(0,val1), max(0,val1))
            return uniform(0, val1)

    def randUniform_array(self, val, mode):
        if isinstance(val, tuple):
            val = list(val)
        if isinstance(val, list):
            tot = np.zeros(len(val)).tolist()
            for i in range(0, len(val)):
                tot[i] = self.choose_uniform_mode(val[i], val[i], mode)
        else:
            tot = self.choose_uniform_mode(val, val, mode)
        return tot

    def init_values(self):
        self.seed = int(time.time() * 1000.0)
        # print("seed: ", self.seed)
        seed(self.seed)
        self.rSplits2 = random()
        self.choiceNegPos1 = choice([-1, 1])
        self.choiceNegPos2 = choice([-1, 1])
        self.randTau1 = self.randUniform_array(tau, 3)
        self.randTau2 = self.randUniform_array(tau, 3)
        self.baseSplits = randint(0, self.maxBaseSplits)
        if self.baseSplits > 0:
            self.splitHeight = 0.6

    def set_variation(self):
        self.init_values()
        zeros_array = [0.0, 0.0, 0.0, 0.0]
        # af3 af4
        temp_af3 = self.af3
        self.af3 = self.randUniform_array(temp_af3, 1)
        self.af4 = self.randUniform_array(temp_af3, 1)

        # rLastAng
        self.rLastAng = self.randUniform_array([360, 360, 360, 360], 3)

        if (self.variateCurve is True):
            temp_curve = self.curve
            self.curve[0] = self.randUniform_array(temp_curve[0], 1)
            self.curveBack[0] = -self.curve[0]

        print(self.curve)

        # curveV1
        # &&& temp_curveV1 = us.toRad(self.curveV)
        temp_curveV1 = us.toRad(self.curve)
        curveV_curveRes1 = np.divide(temp_curveV1, self.curveRes).tolist()
        self.curveV1 = self.randUniform_array(curveV_curveRes1, 3)
        self.curveV1 = us.toDeg(self.curveV1)

        # curveV2
        # &&& temp_curveV2 = us.toRad(self.curveV)
        temp_curveV2 = us.toRad(self.curve)
        curveV_curveRes2 = np.divide(temp_curveV2, self.curveRes).tolist()
        self.curveV2 = self.randUniform_array(curveV_curveRes2, 3)
        self.curveV2 = us.toDeg(self.curveV2)

        # splitAngleV1
        # &&& temp_splitAngleV1 = self.splitAngleV
        temp_splitAngleV1 = self.splitAngle
        self.splitAngleV1 = self.randUniform_array(temp_splitAngleV1, 1)

        # splitAngleV2
        # &&& temp_splitAngleV2 = self.splitAngleV
        temp_splitAngleV2 = self.splitAngle
        self.splitAngleV2 = self.randUniform_array(temp_splitAngleV2, 1)

        self.rotate[0] = self.randUniform_array(360, 3)

        # rotateV
        temp_rotateV = self.rotateV
        # print("rotateV: ", temp_rotateV)
        self.rotateV = self.randUniform_array(temp_rotateV, 1)

        # lengthV
        temp_lengthV = self.lengthV
        # self.lengthV = self.randUniform_array(temp_lengthV, 2)
        self.lengthV = zeros_array

        # leafRotateV
        temp_leafRotateV = self.leafRotateV
        self.leafRotateV = self.randUniform_array(temp_leafRotateV, 1)

        # leafDownAngleV
        temp_leafDownAngleV = self.leafDownAngleV
        if temp_leafDownAngleV > 0.0:
            self.leafDownAngleV = temp_leafDownAngleV
        else:
            self.leafDownAngleV = self.randUniform_array(temp_leafDownAngleV, 1)

        # leafScaleV
        temp_leafScaleV = self.leafScaleV
        self._leafScaleV = self.randUniform_array(temp_leafScaleV, 2)
        # print("temp_leafScalev: ", temp_leafScaleV)
        # print("leafScalev: ", self.leafScaleV)

        # scaleV0
        temp_scaleV0 = self.scaleV0
        self._scaleV0 = self.randUniform_array(temp_scaleV0, 2)

        # downAngleV
        temp_downAngleV = self.downAngleV
        i = 0
        for dav in temp_downAngleV:
            if self.useOldDownAngle is True:
                if dav < 0.0:
                    self.downAngleV[i] = dav
                else:
                    self.downAngleV[i] = self.randUniform_array(dav, 1)
            else:
                if dav < 0.0:
                    self.downAngleV[i] = self.randUniform_array(dav, 1)
                else:
                    self.downAngleV[i] = dav
            i = i + 1

        # scaleV
        temp_scaleV = self.scaleV
        self.scaleV = self.randUniform_array(temp_scaleV, 1)

        # nRings
        if self.nrings > 0:
            temp_nrings = self.nrings
            n_min = temp_nrings - 3
            if n_min < 2:
                n_min = 2
            n_max = temp_nrings + 3
            self.nrings = randint(n_min, n_max)

    def add_tree(self):
        us.addTree(self)
