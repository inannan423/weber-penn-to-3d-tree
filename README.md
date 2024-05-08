# Weber-Penn Parameters to 3D tree model

- [Weber-Penn Parameters to 3D model](#weber-penn-parameters-to-3d-model)
  - [Introduction](#introduction)
    - [Prerequisites](#prerequisites)
    - [Usage](#usage)
  - [中文说明](#中文说明)
    - [前提](#前提)
    - [使用](#使用)

## Introduction

Convert Weber-Penn parameters to 3D tree model in FBX format.

### Prerequisites

- Blender 2.8+, download from [https://www.blender.org/download/](https://www.blender.org/download/), and add it to the environment variable.
- Python 3.7+, download from [https://www.python.org/downloads/](https://www.python.org/downloads/).

Check if Blender has been added to the environment variable:

```bash
blender --version
```

### Usage

```bash
blender -b -P run.py -- --input ./tree/pine.py --output pine
```

- `--input`: The input Weber-Penn parameters file.
- `--output`: The output FBX file name.

## 中文说明

将 Weber-Penn 参数转化为 3D 树木模型（FBX 格式）。

### 前提

- Blender 2.8+，下载地址：[https://www.blender.org/download/](https://www.blender.org/download/)，并将其添加到环境变量中。
- Python 3.7+，下载地址：[https://www.python.org/downloads/](https://www.python.org/downloads/)。

检查 Blender 是否已经添加到环境变量中：

```bash
blender --version
```

### 使用

```bash
blender -b -P run.py -- --input ./tree/pine.py --output pine
```

- `--input`：输入的 Weber-Penn 参数文件。
- `--output`：输出的 FBX 文件名。

## References

- Sapling Tree Gen: From Blender Source Code
- TreeParametersUsingSaplingUtils: From Paper [TreeSketchNet](https://dl.acm.org/doi/10.1145/3579831)