import bpy
import os
import sys
import argparse

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

parser = argparse.ArgumentParser(description="Blender Python Script")

parser.add_argument("--input", help="Input file path")

parser.add_argument("--output", help="Output file path")

args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:])

input_path = args.input

output_path = args.output

print("Input Path:", input_path)

print("Output Path:", output_path)

if input_path is None:
    print("\033[91m" + "Input Path is required" + "\033[0m")
    sys.exit()

if output_path is None:
    print("\033[91m" + "Output Path is required" + "\033[0m")
    sys.exit()

from treeParametersUsingSaplingUtils import TreeParametersUsingSaplingUtils

# 打印 blender 版本
print(bpy.app.version_string)

variateCurve = False
substrings = ["palm", "bamboo", "bonsai"]

# treeName = "1006_bonsai.py"

# if any(x in input_path for x in substrings):
#     variateCurve = True

need_render_tree = TreeParametersUsingSaplingUtils(input_path, variateCurve, output_path)
need_render_tree.load_tree()
need_render_tree.set_variation()
need_render_tree.add_tree()
