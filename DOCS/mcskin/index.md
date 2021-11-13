# mcskin

> Auto-generated documentation for [mcskin](../../mcskin/__init__.py) module.

For some raw skin, generate 1.0, 1.8 and 1.8 bedrock skins.

- [Mcskin](../README.md#mcskin-index) / [Modules](../README.md#mcskin-modules) / mcskin
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
    - Modules
        - [\_\_main\_\_](module.md#__main__)

## cleanImg

[[find in source code]](../../mcskin/__init__.py#L16)

```python
def cleanImg(image: Image.Image, alphaThreshold: int = 225) -> Image.Image:
```

Clean up semi transparent stuff when upscaling and saving with a threshold.

#### Arguments

- `image` *Image.Image* - pil image to clean up
- `alphaThreshold` *int, optional* - threshold. Defaults to 225.

#### Returns

- `Image.Image` - [description]

## cli

[[find in source code]](../../mcskin/__init__.py#L262)

```python
def cli():
```

Cli entry point.

## dumpTex

[[find in source code]](../../mcskin/__init__.py#L240)

```python
def dumpTex(filePath: str):
```

For some raw skin, generate 1.0, 1.8 and 1.8 bedrock skins.

#### Arguments

- `filePath` *str* - path to skin

## getVer

[[find in source code]](../../mcskin/__init__.py#L179)

```python
def getVer(layer: Layer) -> int:
```

Make a guess at the version based on the layer dimensions.

#### Arguments

- `layer` *Layer* - the layer

#### Returns

- `int` - the estimated version

## openRawTex

[[find in source code]](../../mcskin/__init__.py#L214)

```python
def openRawTex(filePath: str) -> LayeredImage:
```

Open texture from a file path

#### Arguments

- `filePath` *str* - path

#### Raises

- `ValueError` - []

#### Returns

- `LayeredImage` - texture

## upgradeLayer

[[find in source code]](../../mcskin/__init__.py#L146)

```python
def upgradeLayer(layer: Layer, target: int = 2) -> Layer | None:
```

Layer to port or upgrade

#### Arguments

- `layer` *Layer* - texture layer to act on
- `target` *int, optional* - target version. Defaults to 2.

#### Returns

Layer | None: Layer or None

## upgradeTex

[[find in source code]](../../mcskin/__init__.py#L195)

```python
def upgradeTex(layeredImage: LayeredImage, target: int = 2) -> LayeredImage:
```

Upgrade/ port a texture

#### Arguments

- `layeredImage` *LayeredImage* - represents the texture
- `target` *int, optional* - target version. Defaults to 2.

#### Returns

- `LayeredImage` - upgraded texture

## ver0to1

[[find in source code]](../../mcskin/__init__.py#L72)

```python
def ver0to1(layer: Layer) -> Layer:
```

Convert a 1.0 skin to 1.8.

#### Arguments

- `layer` *Layer* - texture layer to port

#### Returns

- `Layer` - ported layer

## ver1to0

[[find in source code]](../../mcskin/__init__.py#L99)

```python
def ver1to0(layer: Layer) -> Layer:
```

Convert a 1.8 skin to 1.0.

#### Arguments

- `layer` *Layer* - texture layer to backport

#### Returns

- `Layer` - backport layer

## ver1to2

[[find in source code]](../../mcskin/__init__.py#L36)

```python
def ver1to2(layer: Layer) -> Layer:
```

Convert a 1.8 skin to 1.8_bedrock.

#### Arguments

- `layer` *Layer* - texture layer to upscale

#### Returns

- `Layer` - upscaled layer

## ver2to1

[[find in source code]](../../mcskin/__init__.py#L124)

```python
def ver2to1(layer: Layer) -> Layer:
```

Convert a 1.8_bedrock skin to 1.8.

#### Arguments

- `layer` *Layer* - texture layer to downscale

#### Returns

- `Layer` - downscale layer
