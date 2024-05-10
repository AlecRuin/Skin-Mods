#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Riven/Riven.bin"
    "DATA/Characters/Riven/Animations/Skin0.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin17_Skins_Skin19_Skins_Skin2_Skins_Skin21_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Riven_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin49_Skins_Skin5_Skins_Skin50_Skins_Skin51_Skins_Skin52_Skins_Skin53_Skins_Skin54_Skins_Skin6_Skins_Skin63_Skins_Skin64_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin7_Skins_Skin70_Skins_Skin71_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin21_Skins_Skin24_Skins_Skin25_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin56_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin19_Skins_Skin2_Skins_Skin21_Skins_Skin24_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin56_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin17_Skins_Skin2_Skins_Skin5.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin16_Skins_Skin17_Skins_Skin2_Skins_Skin24_Skins_Skin5_Skins_Skin56.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin17_Skins_Skin19_Skins_Skin2_Skins_Skin21_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin21_Skins_Skin6.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1_Skins_Skin2.bin"
    "DATA/Riven_Skins_Skin0_Skins_Skin1.bin"
}
entries: map[hash,embed] = {
    "Characters/Riven/Skins/Skin0" = SkinCharacterDataProperties {
        SkinClassification: u32 = 1
        ChampionSkinName: string = "BaseRiven"
        MetaDataTags: string = "gender:female,race:human,faction:noxus"
        Loadscreen: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Riven/Skins/Base/RivenLoadScreen.dds"
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Riven"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Riven_Base_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Riven/Skins/Base/Riven_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Riven/Skins/Base/Riven_Base_SFX_events.bnk"
                    }
                    Events: list[string] = {
                        "Play_sfx_Riven_Death3D_cast"
                        "Play_sfx_Riven_Recall3D_buffactivate"
                        "Play_sfx_Riven_RivenBasicAttack2_OnCast"
                        "Play_sfx_Riven_RivenBasicAttack2_OnHit"
                        "Play_sfx_Riven_RivenBasicAttack3_OnCast"
                        "Play_sfx_Riven_RivenBasicAttack3_OnHit"
                        "Play_sfx_Riven_RivenBasicAttack_OnCast"
                        "Play_sfx_Riven_RivenBasicAttack_OnHit"
                        "Play_sfx_Riven_RivenCritAttack_OnCast"
                        "Play_sfx_Riven_RivenCritAttack_OnHit"
                        "Play_sfx_Riven_RivenFeint_OnBuffActivate"
                        "Play_sfx_Riven_RivenFeint_OnBuffDeactivate"
                        "Play_sfx_Riven_RivenFeint_OnCast"
                        "Play_sfx_Riven_RivenFeint_OnHit"
                        "Play_sfx_Riven_RivenFengShuiEngine_OnBuffActivate"
                        "Play_sfx_Riven_RivenFengShuiEngine_OnBuffDeactivate"
                        "Play_sfx_Riven_RivenFengShuiEngine_OnCast"
                        "Play_sfx_Riven_RivenIzunaBlade_OnCast"
                        "Play_sfx_Riven_RivenLightsaberMissile_hit_champ"
                        "Play_sfx_Riven_RivenLightsaberMissile_hit_reg"
                        "Play_sfx_Riven_RivenLightsaberMissile_missilelaunch"
                        "Play_sfx_Riven_RivenLightsaberMissile_OnMissileCast"
                        "Play_sfx_Riven_RivenMartyr_OnCast"
                        "Play_sfx_Riven_RivenMartyr_stun"
                        "Play_sfx_Riven_RivenTriCleave_hit_a"
                        "Play_sfx_Riven_RivenTriCleave_hit_b"
                        "Play_sfx_Riven_RivenTriCleave_hit_ground_lrg"
                        "Play_sfx_Riven_RivenTriCleave_hit_ground_sml"
                        "Play_sfx_Riven_RivenTriCleave_OnCast"
                        "Stop_sfx_Riven_RivenFengShuiEngine_OnBuffActivate"
                    }
                }
                BankUnit {
                    Name: string = "Riven_Base_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Riven/Skins/Base/Riven_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Riven/Skins/Base/Riven_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Riven/Skins/Base/Riven_Base_VO_audio.wpk"
                    }
                    Events: list[string] = {
                        "Play_vo_Riven_Attack2DGeneral"
                        "Play_vo_Riven_Death3D"
                        "Play_vo_Riven_Joke3DGeneral"
                        "Play_vo_Riven_Laugh3DGeneral"
                        "Play_vo_Riven_Move2DStandard"
                        "Play_vo_Riven_RivenBasicAttack2_cast3D"
                        "Play_vo_Riven_RivenBasicAttack3_cast3D"
                        "Play_vo_Riven_RivenBasicAttack_cast3D"
                        "Play_vo_Riven_RivenCritAttack_cast3D"
                        "Play_vo_Riven_RivenFeint_cast3D"
                        "Play_vo_Riven_RivenFengShuiEngine_cast3D"
                        "Play_vo_Riven_RivenIzunaBlade_cast3D"
                        "Play_vo_Riven_RivenMartyr_cast3D"
                        "Play_vo_Riven_RivenTriCleaveSoundOne_OnBuffActivate"
                        "Play_vo_Riven_RivenTriCleaveSoundThree_OnBuffActivate"
                        "Play_vo_Riven_RivenTriCleaveSoundTwo_OnBuffActivate"
                        "Play_vo_Riven_Taunt3DGeneral"
                        "Riven_Switch_NonUlt"
                        "Riven_Switch_Ult"
                    }
                    VoiceOver: bool = true
                }
            }
        }
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = "Characters/Riven/Animations/Skin0"
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Riven/Skins/Base/riven.skl"
            SimpleSkin: string = "ASSETS/Characters/Riven/Skins/Base/riven.skn"
            Texture: string = "ASSETS/Characters/Riven/Skins/Base/Mat_Body.dds"
            SkinScale: f32 = 1.5
            SelfIllumination: f32 = 0.699999988
            ReflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        ArmorMaterial: string = "Flesh"
        DefaultAnimations: list[string] = {
            "Weapon_Snap"
        }
        mContextualActionData: link = "Characters/Riven/CAC/Riven_Base"
        IconCircle: option[string] = {
            "ASSETS/Characters/Riven/HUD/Riven_Circle.dds"
        }
        IconSquare: option[string] = {
            "ASSETS/Characters/Riven/HUD/Riven_Square.dds"
        }
        HealthBarData: embed = CharacterHealthBarDataRecord {
            UnitHealthBarStyle: u8 = 10
        }
        mResourceResolver: link = "Characters/Riven/Skins/Skin0/Resources"
    }
    "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Sword" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "GLOW"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }

                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, -4 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 5 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.294117659, 1, 0.352941185, 0.549019635 }
                }
                ParticleIsLocalOrientation: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -90, 89 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 195, 105, 0 }
                }
                Texture: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_Z_Glow.dds"
                TextureMult: pointer = 0xb097c1bd {
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                }
                MaterialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        Priority: i32 = 1
                        SubMeshName: option[string] = {
                            "Mat_Body"
                        }
                        BaseTexture: string = "ASSETS/Characters/Riven/Skins/Base/Mat_DT.dds"
                        TransitionSample: f32 = 0.1953125
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    9
                }
                IsSingleParticle: flag = true
                EmitterName: string = "SwordFlare_02"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.321568638, 1, 0.321568638, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec4] = {
                            { 0.321568638, 1, 0.321568638, 1 }
                            { 0.321568638, 1, 0.321568638, 0 }
                        }
                    }
                }
                DepthBiasFactors: vec2 = { -1, -5 }
                ParticleIsLocalOrientation: flag = true
                Texture: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_Color-hold.dds"
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_P_MiniSwordMask.dds"
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                EmitterName: string = "GLOW1"
                Importance: u8 = 2
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, -4 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 5 }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.270588249, 1, 0.294117659, 0.34117648 }
                }
                ParticleIsLocalOrientation: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 89 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 195, 105, 0 }
                }
                Texture: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_Z_Glow.dds"
                TextureMult: pointer = 0xb097c1bd {
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 4
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                Lifetime: option[f32] = {
                    15
                }
                EmitterName: string = "Arcs"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 0, 80, 0 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec3] = {
                                { 0, 80, 0 }
                            }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -20, 0 }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.239215687, 1, 0.427450985, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        Values: list[vec4] = {
                            { 0.239215687, 1, 0.427450985, 1 }
                            { 0.239215687, 1, 0.427450985, 1 }
                            { 0.20811601, 0.86999315, 0.371879429, 1 }
                        }
                    }
                }
                Pass: i16 = 30
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_Z_Erosion.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                ParticleIsLocalOrientation: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 180, 180, 180 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 180, 180, 180 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 30, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 30, 30, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Riven/Skins/Base/Particles/Riven_Base_W_Electric_Arcs.dds"
                FrameRate: f32 = 1
                BirthFrameRate: embed = ValueFloat {
                    ConstantValue: f32 = 27
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            27
                        }
                    }
                }
                NumFrames: u16 = 16
                TexDiv: vec2 = { 4, 4 }
            }
        }
        ParticleName: string = "Riven_Base_R_Sword"
        ParticlePath: string = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Sword"
    }
    "Characters/Riven/Skins/Skin0/Resources" = ResourceResolver {
        ResourceMap: map[hash,link] = {
            0x90e17f6e = 0x5d0db0bc
            0xa924a2cc = 0x2befb6ae
            "Riven_BA_Crit_tar" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_BA_Crit_tar"
            "Riven_BA_Tar" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_BA_tar"
            "Riven_E_Mis" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_E_Mis"
            "Riven_E_Shield" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_E_Shield"
            "Riven_P_Buff" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_P_Buff"
            "Riven_Q_01_Detonate" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_01_detonate"
            "Riven_Q_01_Wpn_Trail" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_01_Wpn_Trail"
            "Riven_Q_01_Wpn_Trail_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_01_Wpn_Trail_Ult"
            "Riven_Q_02_Detonate" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_02_detonate"
            "Riven_Q_02_Detonate_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_02_detonate_ult"
            "Riven_Q_02_Wpn_Trail" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_02_Wpn_Trail"
            "Riven_Q_02_Wpn_Trail_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_02_Wpn_Trail_Ult"
            "Riven_Q_03_Detonate" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_03_detonate"
            "Riven_Q_03_Detonate_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_03_detonate_ult"
            "Riven_Q_03_Trail" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_03_trail"
            "Riven_Q_03_Wpn_Trail" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_03_Wpn_Trail"
            "Riven_Q_03_Wpn_Trail_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_03_Wpn_Trail_Ult"
            "Riven_Q_Tar_01" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_tar_01"
            "Riven_Q_tar_02" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_tar_02"
            "Riven_Q_tar_03" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_tar_03"
            "Riven_Q_tar_04" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_tar_04"
            "Riven_R_Buff" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Buff"
            "Riven_R_Mis_Left" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Mis_Left"
            "Riven_R_Mis_Middle" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Mis_Middle"
            "Riven_R_Mis_Right" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Mis_Right"
            "Riven_R_Sword" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Sword"
            "Riven_R_Tar" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Tar"
            "Riven_R_Tar_Minion" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Tar_Minion"
            "Riven_W_Cast" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_W_Cast"
            "Riven_W_Ult_Cas" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_W_Ult_Cas"
            "Riven_W_Ult_Cas_Ground" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_W_Ult_Cas_Ground"
            0x5fbb9070 = "Shared/Particles/Empty"
            "Riven_P_Buff_Wpn" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_P_Buff_Wpn"
            "Riven_R_Buff_L_Hand" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Buff_L_Hand"
            "Riven_R_Buff_R_Hand" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Buff_R_Hand"
            "Riven_R_Buff_Back" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Buff_Back"
            "Riven_R_Cas" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_R_Cas"
            "Riven_Q_detonate_01_Ult" = "Characters/Riven/Skins/Skin0/Particles/Riven_Base_Q_detonate_01_Ult"
        }
    }
}
