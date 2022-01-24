""" tests """
from __future__ import annotations

import sys
from pathlib import Path

import imgcompare
from layeredimage.layeredimage import LayeredImage

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from mcskin import cleanImg, openRawTex, upgradeTex

# Open
layeredImage = openRawTex(f"{THISDIR}/data/template18.png")


def test_layeredImage_is_layeredimage():
	assert isinstance(layeredImage, LayeredImage)


def test_layeredImage_has_1layer():
	assert len(layeredImage.layers) == 1


def test_upgrade_18b():
	img = upgradeTex(layeredImage, 2)
	imgClean = cleanImg(img.getFlattenLayers())
	imgClean.save(f"{THISDIR}/data/out_18b.png")
	assert imgcompare.is_equal(imgClean, f"{THISDIR}/data/out_18b_expected.png")


def test_upgrade_18():
	img = upgradeTex(layeredImage, 1)
	imgClean = cleanImg(img.getFlattenLayers())
	imgClean.save(f"{THISDIR}/data/out_18.png")
	assert imgcompare.is_equal(imgClean, f"{THISDIR}/data/out_18_expected.png")


def test_upgrade_10():
	img = upgradeTex(layeredImage, 0)
	imgClean = cleanImg(img.getFlattenLayers())
	imgClean.save(f"{THISDIR}/data/out_10.png")
	assert imgcompare.is_equal(imgClean, f"{THISDIR}/data/out_10_expected.png")
