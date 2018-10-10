# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from pytest import raises
from loc.locales import Locale
from loc.loc_dict import LocDict


class TestLangDict(object):
    def test_init(self):
        ld1 = LocDict(data={
            Locale.en_US: ["Yes", "No"],
            Locale.zh_CN: ["是", "否"],
        })
        ld2 = LocDict(data=[
            {Locale.en_US: "Yes", Locale.zh_CN: "是"},
            {Locale.en_US: "No", Locale.zh_CN: "否"},
        ])
        assert ld1.data == ld2.data
        assert ld2.locales == ld2.locales

    def test_init_bad_input(self):
        with raises(ValueError):
            LocDict(data={
                Locale.en_US: ["Yes", "No"],
                Locale.zh_CN: ["是", ],
            })

    def test_find_locale(self):
        data = {
            Locale.en_US: ["Yes", "No"],
            Locale.zh_CN: ["是", "否"],
        }
        ld = LocDict(data=data)
        assert ld.find_locale("Yes") == Locale.en_US
        assert ld.find_locale("是") == Locale.zh_CN

        with raises(ValueError):
            ld.find_locale("Not Available")

    def test_trans_to(self):
        data = {
            Locale.en_US: ["Yes", "No"],
            Locale.zh_CN: ["是", "否"],
        }
        ld = LocDict(data=data)

        assert ld.trans_to("Yes", dst_loc=Locale.zh_CN) == "是"
        assert ld.trans_to("Yes", dst_loc=Locale.zh_CN,
                           src_loc=Locale.en_US) == "是"
        assert ld.trans_to("是", dst_loc=Locale.en_US) == "Yes"
        assert ld.trans_to("是", dst_loc=Locale.zh_CN) == "是"

        with raises(ValueError):
            ld.trans_to("是", dst_loc="NA")

        with raises(KeyError):
            ld.trans_to("是", dst_loc=Locale.en_US, src_loc=Locale.en_US)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
