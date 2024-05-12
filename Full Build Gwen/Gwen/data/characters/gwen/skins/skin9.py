#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Gwen/Gwen.bin"
    "DATA/Gwen_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Gwen/Animations/Skin1.bin"
    "DATA/Gwen_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Gwen_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Gwen_Skins_Skin1_Skins_Skin10_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Gwen/Skins/Skin9" = SkinCharacterDataProperties {
        SkinClassification: u32 = 2
        ChampionSkinName: string = "GwenSkin09"
        SkinParent: i32 = 1
        MetaDataTags: string = "gender:female,faction:shadowisles,race:human"
        Loadscreen: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Gwen/Skins/Skin01/GwenLoadScreen_1.dds"
        }
        LoadscreenVintage: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Gwen/Skins/Skin01/GwenLoadscreen_1_LE.dds"
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Gwen"
                "GwenSkin01"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Gwen_Skin01_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Gwen/Skins/Skin01/Gwen_Skin01_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Gwen/Skins/Skin01/Gwen_Skin01_SFX_events.bnk"
                    }
                    Events: list[string] = {
                        "Play_sfx_GwenSkin01_Dance3D_loop"
                        "Play_sfx_GwenSkin01_Death3D_buffactivate"
                        "Play_sfx_GwenSkin01_GwenBasicAttack_Stab_cast"
                        "Play_sfx_GwenSkin01_GwenBasicAttack_Stab_OnHit"
                        "Play_sfx_GwenSkin01_GwenBasicAttack_Swipe_cast"
                        "Play_sfx_GwenSkin01_GwenBasicAttack_Swipe_OnHit"
                        "Play_sfx_GwenSkin01_GwenCritAttack_OnCast"
                        "Play_sfx_GwenSkin01_GwenCritAttack_OnHit"
                        "Play_sfx_GwenSkin01_GwenE2_buffactivate"
                        "Play_sfx_GwenSkin01_GwenE_OnCast"
                        "Play_sfx_GwenSkin01_GwenEEmpoweredAttack_Oncast"
                        "Play_sfx_GwenSkin01_GwenEEmpoweredAttack_OnHitLocation"
                        "Play_sfx_GwenSkin01_GwenEEmpoweredAttack_RResetCannotCancel_Oncast"
                        "Play_sfx_GwenSkin01_GwenEEmpoweredAttack_RResetCannotCancel_OnHitLocation"
                        "Play_sfx_GwenSkin01_GwenQ_max_stacks_buffactivate"
                        "Play_sfx_GwenSkin01_GwenQ_max_stacks_buffactivate_self"
                        "Play_sfx_GwenSkin01_GwenQ_OnCast"
                        "Play_sfx_GwenSkin01_GwenQFirst_cast"
                        "Play_sfx_GwenSkin01_GwenQFirst_hit"
                        "Play_sfx_GwenSkin01_GwenQFirst_hit_center"
                        "Play_sfx_GwenSkin01_GwenQFirst_hit_center_minion"
                        "Play_sfx_GwenSkin01_GwenQFirst_hit_minion"
                        "Play_sfx_GwenSkin01_GwenQLast_cast"
                        "Play_sfx_GwenSkin01_GwenQLast_hit"
                        "Play_sfx_GwenSkin01_GwenQLast_hit_center"
                        "Play_sfx_GwenSkin01_GwenQLast_hit_center_minion"
                        "Play_sfx_GwenSkin01_GwenQLast_hit_minion"
                        "Play_sfx_GwenSkin01_GwenQMiddle_1stack_cast"
                        "Play_sfx_GwenSkin01_GwenQMiddle_2stack_cast"
                        "Play_sfx_GwenSkin01_GwenQMiddle_3stack_cast"
                        "Play_sfx_GwenSkin01_GwenQMiddle_4stack_cast"
                        "Play_sfx_GwenSkin01_GwenQMiddle_hit"
                        "Play_sfx_GwenSkin01_GwenQMiddle_hit_center"
                        "Play_sfx_GwenSkin01_GwenQMiddle_hit_center_minion"
                        "Play_sfx_GwenSkin01_GwenQMiddle_hit_minion"
                        "Play_sfx_GwenSkin01_GwenR1_buffactivate"
                        "Play_sfx_GwenSkin01_GwenR1_buffactivate_self"
                        "Play_sfx_GwenSkin01_GwenR2_buffactivate"
                        "Play_sfx_GwenSkin01_GwenR2_buffactivate_self"
                        "Play_sfx_GwenSkin01_GwenR3_buffactivate"
                        "Play_sfx_GwenSkin01_GwenR3_buffactivate_self"
                        "Play_sfx_GwenSkin01_GwenR3_missile"
                        "Play_sfx_GwenSkin01_GwenR_buffdeactivate"
                        "Play_sfx_GwenSkin01_GwenR_buffdeactivate_self"
                        "Play_sfx_GwenSkin01_GwenR_missile"
                        "Play_sfx_GwenSkin01_GwenR_OnCast"
                        "Play_sfx_GwenSkin01_GwenR_refresh"
                        "Play_sfx_GwenSkin01_GwenR_refresh_self"
                        "Play_sfx_GwenSkin01_GwenRMis_OnHitLocation"
                        "Play_sfx_GwenSkin01_GwenRRecast_OnCast"
                        "Play_sfx_GwenSkin01_GwenW_buffactivate"
                        "Play_sfx_GwenSkin01_GwenW_buffactivate_Self"
                        "Play_sfx_GwenSkin01_GwenW_buffdeactivate"
                        "Play_sfx_GwenSkin01_GwenW_buffdeactivate_Self"
                        "Play_sfx_GwenSkin01_GwenW_cast"
                        "Play_sfx_GwenSkin01_GwenW_champ_enter"
                        "Play_sfx_GwenSkin01_GwenW_champ_enter_other"
                        "Play_sfx_GwenSkin01_GwenW_champ_exit"
                        "Play_sfx_GwenSkin01_GwenW_champ_exit_other"
                        "Play_sfx_GwenSkin01_GwenW_evade"
                        "Play_sfx_GwenSkin01_GwenWRecast_cast"
                        "Play_sfx_GwenSkin01_GwenWRecast_cast_Self"
                        "Play_sfx_GwenSkin01_Idle3D_buffactivate"
                        "Play_sfx_GwenSkin01_Joke3D_buffactivate_loop"
                        "Play_sfx_GwenSkin01_Joke3D_buffactivate_start"
                        "Play_sfx_GwenSkin01_Joke3D_buffactivate_start2"
                        "Play_sfx_GwenSkin01_Joke3D_buffactivate_to_run"
                        "Play_sfx_GwenSkin01_Laugh3D_buffactivate"
                        "Play_sfx_GwenSkin01_Recall3D_buffactivate"
                        "Play_sfx_GwenSkin01_Recall3D_winddown"
                        "Play_sfx_GwenSkin01_Respawn3D_buffactivate"
                        "Play_sfx_GwenSkin01_Taunt3D_buffactivate"
                        "Post_Event_GwenSkin01_GwenW_ambient_ducking"
                        "Stop_sfx_GwenSkin01_GwenBasicAttack_Stab_cast"
                        "Stop_sfx_GwenSkin01_GwenBasicAttack_Swipe_cast"
                        "Stop_sfx_GwenSkin01_GwenW_cast"
                        "Stop_sfx_GwenSkin01_IdleIn3D_buffactivate"
                        "Stop_sfx_GwenSkin01_Joke3D_buffactivate_start"
                        "Stop_sfx_GwenSkin01_Joke3D_buffactivate_start2"
                        "Stop_sfx_GwenSkin01_Joke3D_buffactivate_to_run"
                        "Stop_sfx_GwenSkin01_Recall3D_buffactivate"
                    }
                }
                BankUnit {
                    Name: string = "Gwen_Base_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Gwen/Skins/Base/Gwen_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Gwen/Skins/Base/Gwen_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Gwen/Skins/Base/Gwen_Base_VO_audio.wpk"
                    }
                    Events: list[string] = {
                        "Play_vo_Gwen_Attack2DGeneral"
                        "Play_vo_Gwen_Death3D"
                        "Play_vo_Gwen_FirstEncounter3DAkshan"
                        "Play_vo_Gwen_FirstEncounter3DIrelia"
                        "Play_vo_Gwen_FirstEncounter3DLucian"
                        "Play_vo_Gwen_FirstEncounter3DLux"
                        "Play_vo_Gwen_FirstEncounter3DMalphite"
                        "Play_vo_Gwen_FirstEncounter3DOlaf"
                        "Play_vo_Gwen_FirstEncounter3DOrnn"
                        "Play_vo_Gwen_FirstEncounter3DRiven"
                        "Play_vo_Gwen_FirstEncounter3DSenna"
                        "Play_vo_Gwen_FirstEncounter3DSeraphine"
                        "Play_vo_Gwen_FirstEncounter3DThresh"
                        "Play_vo_Gwen_FirstEncounter3DVayne"
                        "Play_vo_Gwen_FirstEncounter3DVex"
                        "Play_vo_Gwen_FirstEncounter3DViego"
                        "Play_vo_Gwen_FirstEncounter3DYasuo"
                        "Play_vo_Gwen_FirstEncounter3DYorick"
                        "Play_vo_Gwen_GwenBasicAttack2_cast3D"
                        "Play_vo_Gwen_GwenBasicAttack3_cast3D"
                        "Play_vo_Gwen_GwenBasicAttack_cast3D"
                        "Play_vo_Gwen_GwenCritAttack_cast3D"
                        "Play_vo_Gwen_GwenE_cast3D"
                        "Play_vo_Gwen_GwenQ_cast3D"
                        "Play_vo_Gwen_GwenR2_buffactivate_lua"
                        "Play_vo_Gwen_GwenR3_buffactivate_lua"
                        "Play_vo_Gwen_GwenR_cast3D"
                        "Play_vo_Gwen_GwenRRecast_cast3D"
                        "Play_vo_Gwen_GwenRRecast_OnBuffDeactivate"
                        "Play_vo_Gwen_GwenW_cast3D"
                        "Play_vo_Gwen_Joke3DGeneral"
                        "Play_vo_Gwen_JokeResponse3DGeneral"
                        "Play_vo_Gwen_Kill3DAkshan"
                        "Play_vo_Gwen_Kill3DGeneral"
                        "Play_vo_Gwen_Kill3DIrelia"
                        "Play_vo_Gwen_Kill3DLucian"
                        "Play_vo_Gwen_Kill3DLux"
                        "Play_vo_Gwen_Kill3DMalphite"
                        "Play_vo_Gwen_Kill3DOlaf"
                        "Play_vo_Gwen_Kill3DOrnn"
                        "Play_vo_Gwen_Kill3DPenta"
                        "Play_vo_Gwen_Kill3DRiven"
                        "Play_vo_Gwen_Kill3DSenna"
                        "Play_vo_Gwen_Kill3DSeraphine"
                        "Play_vo_Gwen_Kill3DThresh"
                        "Play_vo_Gwen_Kill3DVayne"
                        "Play_vo_Gwen_Kill3DVex"
                        "Play_vo_Gwen_Kill3DViego"
                        "Play_vo_Gwen_Kill3DYasuo"
                        "Play_vo_Gwen_Kill3DYorick"
                        "Play_vo_Gwen_Laugh3DGeneral"
                        "Play_vo_Gwen_Move2DFirst"
                        "Play_vo_Gwen_Move2DLong"
                        "Play_vo_Gwen_Move2DStandard"
                        "Play_vo_Gwen_Recall3DGeneral"
                        "Play_vo_Gwen_Respawn2DGeneral"
                        "Play_vo_Gwen_Taunt3DGeneral"
                        "Play_vo_Gwen_TauntResponse3DGeneral"
                    }
                    VoiceOver: bool = true
                }
            }
        }
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = "Characters/Gwen/Animations/Skin1"
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Gwen/Skins/Skin01/Gwen_Skin01.skl"
            SimpleSkin: string = "ASSETS/Characters/Gwen/Skins/Skin01/Gwen_Skin01.skn"
            Texture: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_TX_CM.dds"
            SelfIllumination: f32 = 0.699999988
            ReflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            InitialSubmeshToHide: string = "Needle Body Skirt Hair"
            SubmeshRenderOrder: string = "Doll, Body, Needle Scissors, Scissors_A_Smear,Skirt,Hair"
            MaterialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_Weapon_TX_CM.dds"
                    Submesh: string = "Scissors"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_Weapon_TX_CM.dds"
                    Submesh: string = "Needle"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_Smears_TX_CM.dds"
                    Submesh: string = "Scissors_A_Smear"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0x5aae789f
                    Submesh: string = "Skirt"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Material: link = 0x98a4da3f
                    Submesh: string = "Hair"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_Doll_TX_CM.dds"
                    Submesh: string = "Doll"
                }
            }
        }
        ArmorMaterial: string = "Flesh"
        IdleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                EffectKey: hash = 0xab030e61
                BoneName: string = "C_Buffbone_Glb_Tiara_Loc"
            }
        }
        IconAvatar: string = "ASSETS/Characters/Gwen/HUD/Gwen_Circle_1.dds"
        mContextualActionData: link = "Characters/Gwen/CAC/Gwen_Base"
        IconCircle: option[string] = {
            "ASSETS/Characters/Gwen/HUD/Gwen_Circle_0.dds"
        }
        IconSquare: option[string] = {
            "ASSETS/Characters/Gwen/HUD/Gwen_Square_0.dds"
        }
        GodrayFxBone: string = ""
        HealthBarData: embed = CharacterHealthBarDataRecord {
            AttachToBone: string = "Buffbone_Cstm_Healthbar"
            UnitHealthBarStyle: u8 = 9
        }
        mResourceResolver: link = "Characters/Gwen/Skins/Skin9/Resources"
    }
    0x5aae789f = StaticMaterialDef {
        Name: string = "Characters/Gwen/Skins/Skin9/Materials/Outline_Iridescent_Add_Scroll_Skirt_inst"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture"
                TextureName: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_TX_CM.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "iridescentTex"
                TextureName: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_Smears_TX_CM.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScrollTex"
                TextureName: string = "ASSETS/Shared/Materials/white.dds"
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScroll_Mask"
                TextureName: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin9_TX_Mask.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture2"
                TextureName: string = "ASSETS/Shared/Materials/black.PIE_C_13_24.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "OutlineColor"
                Value: vec4 = { 0.109803922, 1, 0.333333343, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineThickness"
                Value: vec4 = { 0.292499989, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineSoftness"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexTile"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "IridescentControl"
                Value: vec4 = { 0.699999988, 0.5, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_R"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "TintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_R"
                Value: vec4 = { 1, 0, 0.400000006, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_R"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_Tex_BlendVlue"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Color"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_ON"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENCE_OUTLINE"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "DIFFUSE_LERP_ON"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_MASK_ON"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "INVERT_BLOOM_FRESNEL"
                On: bool = false
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = 0x6b122501
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    0x98a4da3f = StaticMaterialDef {
        Name: string = "Characters/Gwen/Skins/Skin9/Materials/Outline_Iridescent_Add_Scroll_inst"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture"
                TextureName: string = "ASSETS/Characters/Gwen/Skins/Skin09/Gwen_Skin09_TX_CM.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "iridescentTex"
                TextureName: string = "ASSETS/Characters/Gwen/Skins/Skin01/Gwen_Skin01_Iridescence_Plum.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScrollTex"
                TextureName: string = "ASSETS/Shared/Materials/white.dds"
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScroll_Mask"
                TextureName: string = "ASSETS/Shared/Materials/white.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture2"
                TextureName: string = "ASSETS/Shared/Materials/black.PIE_C_13_24.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "OutlineColor"
                Value: vec4 = { 0, 1, 0.549019635, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineThickness"
                Value: vec4 = { 0.237499997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineSoftness"
                Value: vec4 = { 0.482499987, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexTile"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "IridescentControl"
                Value: vec4 = { 0.5, 0.899999976, 0.5, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_R"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "TintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_R"
                Value: vec4 = { 0.352941185, 0, 0.294117659, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_R"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Diffuse_Tex_BlendVlue"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_A"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Color"
            }
            StaticMaterialShaderParamDef {
                Name: string = "Bloom_Intensity"
            }
        }
        Switches: list2[embed] = {
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_ON"
            }
            StaticMaterialSwitchDef {
                Name: string = "IRIDESCENCE_OUTLINE"
            }
            StaticMaterialSwitchDef {
                Name: string = "DIFFUSE_LERP_ON"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_MASK_ON"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "INVERT_BLOOM_FRESNEL"
                On: bool = false
            }
        }
        ShaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        Techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                Name: string = "normal"
                Passes: list[embed] = {
                    StaticMaterialPassDef {
                        Shader: link = 0x6b122501
                        BlendEnable: bool = true
                        SrcColorBlendFactor: u32 = 6
                        SrcAlphaBlendFactor: u32 = 6
                        DstColorBlendFactor: u32 = 7
                        DstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        ChildTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                Name: string = "transition"
                ParentName: string = "normal"
                ShaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
    "Characters/Gwen/Skins/Skin9/Resources" = ResourceResolver {
        ResourceMap: map[hash,link] = {
            0x114bf027 = 0x5b3bd775
            0x3cf034bd = 0xed97918b
            0xd6f97d52 = 0x66e1b9e4
            0x6c25c5fd = 0xedcf3fc7
            0x54f25475 = 0xfe117ff3
            0xf46b6c2e = 0x5ebf8d28
            0x348e95e9 = 0x4bbc083b
            0x5063038a = 0x2a0dd534
            0xc02e013a = 0x5f35adf0
            0x645b0548 = 0xecbfe826
            0x5489e702 = "Characters/Gwen/Skins/Skin0/Particles/Gwen_Base_W_Missile_Overlay"
            0x95772ddf = 0x3ad532cd
            0x8acf15dc = 0x526bc342
            0x197568bb = 0x0e5dce79
            0x1a756a4e = 0x0b5dc9c0
            0x1b756be1 = 0x0c5dcb53
            0x2e05659c = 0x28f02fda
            0x300568c2 = 0x26f02cb4
            0x31056a55 = 0x27f02e47
            0x3d021ae0 = 0xccea35a2
            0xadd0691d = 0xf5c3abd3
            0xfa095bb3 = 0xff254bd9
            0x6052a5ec = 0xde2811e2
            0x40021f99 = 0xcbea340f
            0xbb89a3ec = 0xbc3c19ce
            0x069b7564 = 0xb9b6d2e2
            0x099b7a1d = 0xb8b6d14f
            0x6b7bfdee = 0xb5cd77bc
            0x3c3429cc = 0x15a45eba
            0xf85c65e0 = 0x197a90a6
            0x7e87a8f0 = 0x994c78a6
            0x345d9296 = 0x8b64e664
            0x52d46747 = 0xd50fff61
            0xdcc535cb = 0x48345155
            0xb493fb82 = 0x46a8c16c
            0x2e82aa72 = 0x439b12b8
            0xb393f9ef = 0x49a8c625
            0xd2506fc3 = 0xdf66ce45
            0x15f8c2fb = 0x77de0b05
            0x335d9103 = 0x8e64eb1d
            0x325d8f70 = 0x8d64e98a
            0x5da9e144 = 0xf6c66a6a
            0x60a9e5fd = 0xf5c668d7
            0x7ba914f5 = 0xc0140f3f
            0x3cdff572 = 0x0963e924
            0xb15ef221 = "Characters/Gwen/Skins/Skin0/Particles/Gwen_Base_Emote_Hand_Trail01"
            0xfe5b596d = 0xd758cdc3
            0xb752efd4 = 0x02c1b2d2
            0xd9c12ee6 = 0xef209398
            0xfa537508 = 0x9d0d4bc2
            0x8bd15598 = 0x01fe9d8e
            0x995f1bc0 = 0x1527c59a
            0xe2662f7a = "Characters/Gwen/Skins/Skin0/Particles/Gwen_Base_Emote_Taunting_Visuals"
            0xc05c6677 = "Characters/Gwen/Skins/Skin0/Particles/Gwen_Base_Emote_Joking_Dustkick"
            0xc571b896 = 0x22b69bc0
            0xa2587bdc = 0x12600a92
            0xf3319a82 = 0x9db9d8dc
            0xbc7ba71d = 0xbf08cd83
            0xb97ba264 = 0xc008cf16
            0xab030e61 = 0x58be1bab
            0x49d35a20 = 0x10b5e3ca
            0x9e53cf71 = 0x8ce18b47
            0xae4fd93b = 0x3eeec661
            0x44291ab8 = 0xa07b6d36
            0x6c67000d = 0xb5fedd23
            0x44071d7b = 0x193bc4b9
            0x9ee1d7ae = 0x997be838
        }
    }
}
