# Mcskin

[Mcskin Index](../README.md#mcskin-index) / Mcskin

> Auto-generated documentation for [mcskin](../../../mcskin/__init__.py) module.

- [Mcskin](#mcskin)
  - [cleanImg](#cleanimg)
  - [cli](#cli)
  - [dumpTex](#dumptex)
  - [getVer](#getver)
  - [openRawTex](#openrawtex)
  - [upgradeLayer](#upgradelayer)
  - [upgradeTex](#upgradetex)
  - [ver0to1](#ver0to1)
  - [ver1to0](#ver1to0)
  - [ver1to2](#ver1to2)
  - [ver2to1](#ver2to1)
  - [Modules](#modules)

## cleanImg

[Show source in __init__.py:16](../../../mcskin/__init__.py#L16)

Clean up semi transparent stuff when upscaling and saving with a threshold.

#### Arguments

- `image` *Image.Image* - pil image to clean up
- `alphaThreshold` *int, optional* - threshold. Defaults to 205.

#### Returns

- `Image.Image` - [description]

#### Signature

```python
def cleanImg(image: Image.Image, alphaThreshold: int = 205) -> Image.Image: ...
```



## cli

[Show source in __init__.py:266](../../../mcskin/__init__.py#L266)

Cli entry point.

#### Signature

```python
def cli(): ...
```



## dumpTex

[Show source in __init__.py:240](../../../mcskin/__init__.py#L240)

For some raw skin, generate 1.0, 1.8 and 1.8 bedrock skins.

#### Arguments

- `filePath` *str* - path to skin

#### Signature

```python
def dumpTex(filePath: str): ...
```



## getVer

[Show source in __init__.py:179](../../../mcskin/__init__.py#L179)

Make a guess at the version based on the layer dimensions.

#### Arguments

- `layer` *Layer* - the layer

#### Returns

- `int` - the estimated version

#### Signature

```python
def getVer(layer: Layer) -> int: ...
```



## openRawTex

[Show source in __init__.py:214](../../../mcskin/__init__.py#L214)

Open texture from a file path

#### Arguments

- `filePath` *str* - path

#### Raises

- `ValueError` - []

#### Returns

- `LayeredImage` - texture

#### Signature

```python
def openRawTex(filePath: str) -> LayeredImage: ...
```



## upgradeLayer

[Show source in __init__.py:146](../../../mcskin/__init__.py#L146)

Layer to port or upgrade

#### Arguments

- `layer` *Layer* - texture layer to act on
- `target` *int, optional* - target version. Defaults to 2.

#### Returns

Layer | None: Layer or None

#### Signature

```python
def upgradeLayer(layer: Layer, target: int = 2) -> Layer | None: ...
```



## upgradeTex

[Show source in __init__.py:195](../../../mcskin/__init__.py#L195)

Upgrade/ port a texture

#### Arguments

- `layeredImage` *LayeredImage* - represents the texture
- `target` *int, optional* - target version. Defaults to 2.

#### Returns

- `LayeredImage` - upgraded texture

#### Signature

```python
def upgradeTex(layeredImage: LayeredImage, target: int = 2) -> LayeredImage: ...
```



## ver0to1

[Show source in __init__.py:72](../../../mcskin/__init__.py#L72)

Convert a 1.0 skin to 1.8.

#### Arguments

- `layer` *Layer* - texture layer to port

#### Returns

- `Layer` - ported layer

#### Signature

```python
def ver0to1(layer: Layer) -> Layer: ...
```



## ver1to0

[Show source in __init__.py:99](../../../mcskin/__init__.py#L99)

Convert a 1.8 skin to 1.0.

#### Arguments

- `layer` *Layer* - texture layer to backport

#### Returns

- `Layer` - backport layer

#### Signature

```python
def ver1to0(layer: Layer) -> Layer: ...
```



## ver1to2

[Show source in __init__.py:36](../../../mcskin/__init__.py#L36)

Convert a 1.8 skin to 1.8_bedrock.

#### Arguments

- `layer` *Layer* - texture layer to upscale

#### Returns

- `Layer` - upscaled layer

#### Signature

```python
def ver1to2(layer: Layer) -> Layer: ...
```



## ver2to1

[Show source in __init__.py:124](../../../mcskin/__init__.py#L124)

Convert a 1.8_bedrock skin to 1.8.

#### Arguments

- `layer` *Layer* - texture layer to downscale

#### Returns

- `Layer` - downscale layer

#### Signature

```python
def ver2to1(layer: Layer) -> Layer: ...
```



## Modules

- [Module](./module.md)