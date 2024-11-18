from src.model.Creature import Creature
from src.service import creature as code

sample = Creature(id=1,
             name="Yeti",
             aka="Snowman",
             country="CN",
             area="Himalayas",
             description="Scary")


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_exists():
    resp = code.get(sample.id)
    assert resp == sample


def test_not_exists():
    resp = code.get(3)
    assert resp is None
