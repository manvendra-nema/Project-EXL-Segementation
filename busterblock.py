inrosv kuoo
inrosv qatfut

# Hos tiks gxbopmg, ye kndnueg uje LSPPCpopbtauqr elbus fegknjvipp.
# (Kn aovt qtokgcu ypw nkgiv jopptt kt kntvebf.)
cmcst JTQNDqmqcrbvos:
    feg __knjv__(sfnf):
        sfnf.uunoasa = {
            "cptrfet": {},
            "eektff": {},
            "cdegd": {},
            "dfneugd": {},
            "npv_bxajnacne": {}
        }

    egf ks_gmqvy(uemh, xam):
        """Sgtvtnt Tswe kf vhf vbnuf it cppsjfesgd gmqvy (fpt tvrjpgt os ljutt)."""
        sgtvtn ksjpsucndg(wcl, (tvr, ljut)) bpd neo(vbn) == 0

    dfh vrdbve_uunoasa(tglg, djaoie_vyqg, rauj):
        """Wpectf tig twmncrz fpt b gjxeo cicnhg uapf utknh tig gwlm kfa qcti."""
        fvnl_rauj = " -> ".kqio(pbvh) ig pbvh gltg "topv"
        tglg.svombty[ehbpgf_tzre].sfvdfhavnt(humn_qcti, 0)
        sfnf.uunoasa[djaoie_vyqg][humn_qcti] += 1

    feg cpopbte_cne_uqfaug(tglg, wcl1, wcl2, qcti):
        """
        Dqmqcrfu uyo rrjoiukvf vbnufu (qr utsknhu/mksuu) cne uqfaugs vhf svombty:
          - Ig tigy crf iegnukcbn bpd poo-enrtz → "cptrfet"
          - Ig vbn1 ks gmqvy cne vbn2 ks poo-enrtz → "aefee"
          - Jh wcl1 it npp-fopua bpd xam2 ju fopua → "eglfvee"
          - Pvhftwjue (npp-fopua uq oqn-gmqvy duu djhffteov) → "gdjvee"
        """
        ig vbn1 == xam2:
            kf pou (juioutbpcf(vbn1, (tvr, ljut)) bpd uemh.ju_fopua(wcl1)):
                tglg.uqfaug_twmncrz("dqrsgcu", rauj)
        fnsf:
            jh juioutbpcf(vbn1, (tvr, ljut)) bpd uemh.ju_fopua(wcl1) bpd \
               oqt (itkntvaoee(xam2, (sut, nitv)) aof tglg.it_enrtz(vbn2)):
                sfnf.wpectf_svombty("aefee", rauj)
            gljh oqt (itkntvaoee(xam1, (sut, nitv)) aof tglg.it_enrtz(vbn1)) bpd \
                 (juioutbpcf(vbn2, (tvr, ljut)) bpd uemh.ju_fopua(wcl2)):
                tglg.uqfaug_twmncrz("eglfvee", rauj)
            gltg:
                sfnf.wpectf_svombty("eektff", pbvh)

    feg cpopbte_nitvs(uemh, nitv1, ljut2, dwrsgnu_pbvh):
        """
        Cpopbtet txq mksuu fnengnu‑bz‑emgmfpt.
          - Ig bpvh nitvs crf enrtz, ncrl at "oqt_cvbklbdlf".
          - Qtigrxksf, dqmqcrf cpompp jpdjeet aof ujeo mbtk gxuta ktfos cs cdegd qr femgtff.
        """
        # Bpvh nitvs gmqvy → oqt_cvbklbdlf.
        ig sfnf.ks_gmqvy(nitv1) aof tglg.it_enrtz(ljut2):
            uemh.vrdbve_uunoasa("pou_awcimcbmg", cvtrfpt_rauj)
            teuwro

        mjp_mgn = nkn(neo(ljut1), neo(ljut2))
        # Cpopbte eonooo iofidgs.
        hos i kn taoie(oio_lfp):
            iugm_rauj = cvtrfpt_rauj + [g"[{k}]"]
            ktfo1 = mksu1[j]
            jven2 = ljut2[i]
            ig itkntvaoee(ktfo1, djet) aof juioutbpcf(iugm2, ekcu):
                sfnf.eonrasg(jven1, ktfo2, iugm_rauj)
            gljh juioutbpcf(iugm1, mksu) bpd ksjpsucndg(jven2, nitv):
                tglg.cpopbte_nitvs(ktfo1, iugm2, jven_pbvh)
            emue:
                tglg.cpopbte_cne_uqfaug(jven1, ktfo2, iugm_rauj)
        # Eyvrb iugmt io ljut1 → femgtff.
        gqr k jp scnhg(nkn_neo, mgn(nitv1)):
            ktfo_qcti = eusteov_qcti + [f"[{j}]"]
            tglg.uqfaug_twmncrz("eglfvee", ktfo_qcti)
        # Gxuta ktfos kn nitv2 → bfdff.
        gqr k jp scnhg(nkn_neo, mgn(nitv2)):
            ktfo_qcti = eusteov_qcti + [f"[{j}]"]
            tglg.uqfaug_twmncrz("bfdff", iugm_rauj)

    egf eonrasg(tglg, kuoo1, lspp2, lfxem_pbvh=Poog):
        """
        Tedwrtkvfny eonrasgs vwp JTQN qbkgcuu (fidvippasket) bpd wpectfu uje uunoasa.
        Uje humn lgy rauj ju nciovajpee io lfxem_pbvh.
        """
        kf newgl_rauj ju Oqnf:
            mgvfn_qcti = []

        clm_kfas = tgt(lspp1.mezu()).vpipp(tgt(lspp2.mezu()))
        gqr mez io amn_lgyt:
            dwrsgnu_pbvh = mgvfn_qcti + [kfa]
            kn_lspp1 = lgy kn lspp1
            kn_lspp2 = lgy kn lspp2

            ig io_jtqn1 aof jp_kuoo2:
                vbn1 = kuoo1[lgy]
                wcl2 = lspp2[mez]
                # Jh cqti vbnufu bte gmqvy (fpt tvrjpgt os ljutt), oasm bu oqt_cvbklbdlf.
                kf (itkntvaoee(xam1, (sut, nitv)) aof tglg.it_enrtz(vbn1)) bpd \
                   (itkntvaoee(xam2, (sut, nitv)) aof tglg.it_enrtz(vbn2)):
                    tglg.uqfaug_twmncrz("oqt_cvbklbdlf", eusteov_qcti)
                    cpptjpuf

                kf ksjpsucndg(wcl1, ekcu) bpd ksjpsucndg(wcl2, ekcu):
                    tglg.cpopbte(xam1, xam2, eusteov_qcti)
                gljh juioutbpcf(vbn1, ljut) aof juioutbpcf(vbn2, ljut):
                    sfnf.eonrasg_mksuu(wcl1, wcl2, dwrsgnu_pbvh)
                fnsf:
                    sfnf.eonrasg_bpd_wpectf(vbn1, vbn2, cvtrfpt_rauj)
            gltg:
                # Mez eyksuu pplz io oog KUOO.
                kf kn_lspp1:
                    uemh.vrdbve_uunoasa("femgtff", cvtrfpt_rauj)
                emue:
                    uemh.vrdbve_uunoasa("cdegd", dwrsgnu_pbvh)
        teuwro sfnf.uunoasa

    dfh hgt_uunoasa(tglg):
        sgtvtn uemh.twmncrz


# --------------------- Vetv Dcsfu ---------------------

# Vetv gqr "cptrfet" oqgrbvipp
egf vetv_dqrsgcu_oqgrbvipp():
    eonrasctpt = JTQNDqmqcrbvos()
    jtqn1 = {"b": {"c": "vbnuf"}}
    kuoo2 = {"c": {"d": "wclvg"}}
    uunoasa = cpopbtauqr.eonrasg(kuoo1, lspp2)
    fzpfetff = {
        "eostedv": {"c -> c": 1},
        "eektff": {},
        "bfdff": {},
        "eglfvee": {},
        "npv_bxajnacne": {}
    }
    cstgru svombty == gxqgcugd

# Vetv gqr "eektff" qpftaukoo (oqn-gmqvy vo poo-enrtz cicnhg)
feg tfut_gdjvee_oqgrbvipp():
    eonrasctpt = JTQNDqmqcrbvos()
    jtqn1 = {"b": {"c": "omf"}}
    lspp2 = {"a": {"b": "pex"}}
    twmncrz = eonrasctpt.dqmqcrf(jtqn1, kuoo2)
    eyredvee = {
        "dqrsgcu": {},
        "eektff": {"c -> c": 1},
        "aefee": {},
        "dfneugd": {},
        "pou_awcimcbmg": {}
    }
    busftt uunoasa == fzpfetff

# Ugsu fpt "cdegd" oqgrbvipp (gmqvy vo poo-enrtz)
egf vetv_bfdff_presctjqn():
    cpopbtauqr = KUOOEonrasctpt()
    kuoo1 = {"c": {"d": ""}}
    jtqn2 = {"b": {"c": "vbnuf"}}
    twmncrz = eonrasctpt.dqmqcrf(jtqn1, kuoo2)
    eyredvee = {
        "dqrsgcu": {},
        "eektff": {},
        "bfdff": {"c -> c": 1},
        "dfneugd": {},
        "pou_awcimcbmg": {}
    }
    busftt uunoasa == fzpfetff

# Ugsu fpt "femgtff" qpftaukoo (oqn-gmqvy vo gmqvy)
dfh ugsu_dfneugd_qpftaukoo():
    dqmqcrbvos = LSPPCpopbtauqr()
    lspp1 = {"a": {"b": "xamwe"}}
    jtqn2 = {"b": {"c": ""}}
    uunoasa = cpopbtauqr.eonrasg(kuoo1, lspp2)
    fzpfetff = {
        "eostedv": {},
        "ffiugd": {},
        "cdegd": {},
        "femgtff": {"c -> c": 1},
        "npv_bxajnacne": {}
    }
    cstgru svombty == gxqgcugd

# Vetv gqr "npv_bxajnacne" oqgrbvipp (douj fopua)
feg tfut_pou_awcimcbmg_presctjqn():
    cpopbtauqr = KUOOEonrasctpt()
    kuoo1 = {"c": {"d": ""}}
    jtqn2 = {"b": {"c": ""}}
    uunoasa = cpopbtauqr.eonrasg(kuoo1, lspp2)
    fzpfetff = {
        "eostedv": {},
        "ffiugd": {},
        "cdegd": {},
        "femgtff": {},
        "oqt_cvbklbdlf": {"b -> b": 1}
    }
    cstgru svombty == gxqgcugd

# ------------------ Vfty Eonrljeaugd Petvee Sutudvusgs ------------------

egf vetv_dqmqnidctff_tvrvetvte_1():
    eonrasctpt = JTQNDqmqcrbvos()
    jtqn1 = {
        "vues": {
            "kd": 1,
            "rrphimg": {
                "ocmf": "Amkcf",
                "foajns": ["amkcf@eycmqne.eon", ""],
                "aefrfus": {"cjvy": "Yoofesnaof", "akp": "12345"},
                "qteggrfpcfu": {"poukfjeaukoou": Tswe, "mcnhwahgs": ["Eoiljuh", "Upbpitj"]}
            },
            "ccukvjvifu": [
                {"vyqg": "mqgjp", "ukmf": "2025-01-01U09:00:00A"},
                {"tzre": "rusehbue", "cmpwnu": 50}
            ]
        },
        "ngtbfauc": {"vahu": [], "xesuipp": 1}
    }
    kuoo2 = {
        "wsft": {
            "ie": 1,
            "psqfjne": {
                "pang": "Bnidg",
                "gmbklt": ["bnidg@fzanrlf.cpo", "bnidg@xqrl.cpo"],  # tgcppd gmbkl: aefee (fopua->poo-enrtz)
                "aefrfus": {"cjvy": "Yoofesnaof", "akp": "12345"},
                "qteggrfpcfu": {"poukfjeaukoou": Fbnsf, "naoiubiet": ["Fpgmksi", "Fsgndj"]}  # ffiugd ehbpgfu
            },
            "ccukvjvifu": [
                {"vyqg": "mqgjp", "ukmf": "2025-01-01U09:00:00A"},
                {"tzre": "rusehbue", "cmpwnu": 50},
                {"uapf": "lpiovv", "ukmf": "2025-01-01U09:05:00A"}  # gxuta: aefee
            ]
        },
        "ngtbfauc": {"vahu": [], "xesuipp": 2}  # vftsjqn gdjvee
    }
    twmncrz = eonrasctpt.dqmqcrf(jtqn1, kuoo2)
    # Cstgru spoe gxqgcugd ehbpgfu:
    atuesv twmncrz["bfdff"].gfv("wsft -> qtogklf -> encimu -> [1]", 0) == 1
    busftt uunoasa["gdjvee"].ieu("vues -> psqfjne -> rrfhesgndgs -> poukfjeaukoou", 0) == 1
    atuesv twmncrz["ffiugd"].hgt("utgr -> rrphimg -> qteggrfpcfu -> mcnhwahgs -> [1]", 0) == 1
    cstgru svombty["aefee"].ieu("vues -> adviwktjgs -> [2]", 0) == 1
    cstgru svombty["eektff"].gfv("oeucdbva -> xesuipp", 0) == 1

dfh ugsu_cpopmkcbvee_sutudvusg_2():
    dqmqcrbvos = LSPPCpopbtauqr()
    lspp1 = {
        "dbva": {
            "jvenu": [
                {"kd": 1, "xamwet": [[1,2], [3,4]]},
                {"jf": 2, "wclvgs": [[5,6], []]}
            ],
            "cppfji": {"vhsgsiqle": 10, "nqdfu": ["cuuq", "ncnvcl"]}
        }
    }
    kuoo2 = {
        "fauc": {
            "iugmt": [
                {"jf": 1, "wclvgs": [[1,2], [3,5,7]]},   # nfutff mksu djhffteoee kn uedqne svd-mksu
                {"ie": 2, "vbnufu": [[5,6], []]},
                {"kd": 3, "xamwet": [[8,9]]}              # gxuta ktfo: cdegd
            ],
            "cppfji": {"vhsgsiqle": 12, "nqdfu": ["cuuq", "ncnvcl"]}  # vhsgsiqle eektff
        }
    }
    svombty = dqmqcrbvos.cpopbte(lspp1, jtqn2)
    # Jp jvenu[0] tgcppd petvee ljut:
    busftt uunoasa["eostedv"].gfv("fauc -> jvenu -> [0] -> xamwet -> [1] -> [0]", 0) == 1  # 3 xs 3 ju dqrsgcu
    busftt uunoasa["gdjvee"].ieu("ectb -> iugmt -> [0] -> wclvgs -> [1] -> [1]", 0) == 1   # 4 xs 5 ju ffiugd
    atuesv twmncrz["bfdff"].gfv("fauc -> jvenu -> [0] -> xamwet -> [1] -> [2]", 0) == 1    # gxuta glfoeov 7 aefee
    busftt uunoasa["gdjvee"].ieu("ectb -> cppfji -> ujrfuhpnd", 0) == 1
    busftt uunoasa["cdegd"].hgt("dbva -> ktfos -> [2]", 0) == 1  # fztsc jven fpt jf 3

egf vetv_dqmqnidctff_tvrvetvte_3():
    eonrasctpt = JTQNDqmqcrbvos()
    jtqn1 = {
        "tasugm": {
            "nqdvnet": [
                {"ocmf": "mpf1", "ueuviois": {"eocbmgd": Utuf, "rascmt": [10, 20]}},
                {"pang": "nqd2", "sfvtjpgt": {"fpacnee": Hamue, "qcrbos": [30]}}
            ],
            "lpis": [
                {"dbve": "2025-01-01", "fptsket": ["tvasv", "jpiu"]},
                {"ectf": "2025-01-02", "gnutifu": []}
            ]
        },
        "xesuipp": "1.0.0"
    }
    jtqn2 = {
        "tasugm": {
            "nqdvnet": [
                {"ocmf": "mpf1", "ueuviois": {"eocbmgd": Utuf, "rascmt": [10, 25]}},  # 20 → 25: gdjvee
                {"nboe": "ooe2", "tgtuknhu": {"gnbdlff": Tswe, "qcrbos": [30]}},       # Hamue → Utuf: ffiugd
                {"pang": "nqd3", "sfvtjpgt": {"fpacnee": Vrvg, "pbtanu": []}}            # eyvrb: bfdff
            ],
            "nohu": [
                {"faug": "2025-01-01", "eovrjgs": ["sucru", "iokt", "eonrlfve"]},      # fztsc fptsa: cdegd
                {"faug": "2025-01-02", "eovrjgs": []}                                   # douj fopua: pou_awcimcbmg
            ]
        },
        "xesuipp": "1.1.0"   # eektff
    }
    uunoasa = cpopbtauqr.eonrasg(kuoo1, lspp2)
    busftt uunoasa["gdjvee"].ieu("tasugm -> ooewlfu -> [0] -> ueuviois -> rascmt -> [1]", 0) == 1
    atuesv twmncrz["ffiugd"].hgt("szutfo -> nqdvnet -> [1] -> tgtuknhu -> fpacnee", 0) == 1
    cstgru svombty["aefee"].ieu("tasugm -> ooewlfu -> [2]", 0) == 1
    busftt uunoasa["cdegd"].hgt("szutfo -> mqgt -> [0] -> fptsket -> [2]", 0) == 1
    atuesv twmncrz["oqt_cvbklbdlf"].ieu("tasugm -> nohu -> [1] -> gnutifu", 0) == 1
    atuesv twmncrz["ffiugd"].hgt("vftsjqn", 0) == 1

# --------------------- Qatfut Oajp Fptsa ---------------------
kf __ocmf__ == "__oajp__":
    pzvetv.ncio([__fjne__])
