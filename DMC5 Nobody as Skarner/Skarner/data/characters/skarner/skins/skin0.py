#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Skarner/Skarner.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Skarner_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Skarner/Animations/Skin0.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin2.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Skarner_Skins_Skin0_Skins_Skin2_Skins_Skin3.bin"
}
entries: map[hash,embed] = {
    "Characters/Skarner/Skins/Skin0" = SkinCharacterDataProperties {
        SkinClassification: u32 = 1
        ChampionSkinName: string = "SkarnerBase"
        MetaDataTags: string = "faction:ixtal"
        SkinUpgradeData: embed = SkinUpgradeData {
            mGearSkinUpgrades: list[link] = {
                0xacec80cb
                0x9da3c2da
            }
        }
        Loadscreen: embed = CensoredImage {
            Image: string = "ASSETS/Characters/Skarner/Skins/Base/SkarnerLoadScreen_0.Skarner_Rework.dds"
        }
        SkinAudioProperties: embed = SkinAudioProperties {
            TagEventList: list[string] = {
                "Skarner"
            }
            BankUnits: list2[embed] = {
                BankUnit {
                    Name: string = "Skarner_Base_SFX"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Skarner/Skins/Base/Skarner_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Skarner/Skins/Base/Skarner_Base_SFX_events.bnk"
                    }
                    Events: list[string] = {
                        "Play_sfx_Skarner_Dance3D_var1_buffactivate"
                        "Play_sfx_Skarner_Dance3D_var2_buffactivate"
                        "Play_sfx_Skarner_Death3D_buffactivate"
                        "Play_sfx_Skarner_E_warning_loop"
                        "Play_sfx_Skarner_Emote3D_rock"
                        "Play_sfx_Skarner_Joke3D_buffactivate"
                        "Play_sfx_Skarner_Laugh3D_buffactivate"
                        "Play_sfx_Skarner_Recall3D_buffactivate"
                        "Play_sfx_Skarner_Recall3D_winddown"
                        "Play_sfx_Skarner_SkarnerE_hit"
                        "Play_sfx_Skarner_SkarnerEGrab_buffactivate"
                        "Play_sfx_Skarner_SkarnerEMovement_footstep"
                        "Play_sfx_Skarner_SkarnerEMovement_loop"
                        "Play_sfx_Skarner_SkarnerEMovement_wall_exit"
                        "Play_sfx_Skarner_SkarnerP_loop"
                        "Play_sfx_Skarner_SkarnerQ_buffdeactivate"
                        "Play_sfx_Skarner_SkarnerQ_timer"
                        "Play_sfx_Skarner_SkarnerQThrow_hit"
                        "Play_sfx_Skarner_SkarnerQThrow_missilelaunch"
                        "Play_sfx_Skarner_SkarnerQThrow_obd"
                        "Play_sfx_Skarner_SkarnerR_buffactivate"
                        "Play_sfx_Skarner_SkarnerR_buffdeactivate"
                        "Play_sfx_Skarner_SkarnerR_cast"
                        "Play_sfx_Skarner_SkarnerR_hit"
                        "Play_sfx_Skarner_SkarnerR_hitlocation"
                        "Play_sfx_Skarner_SkarnerR_missilelaunch"
                        "Play_sfx_Skarner_SkarnerW_hit"
                        "Play_sfx_Skarner_SkarnerW_missilelaunch"
                        "Play_sfx_Skarner_SkarnerW_OnCast"
                        "Play_sfx_Skarner_Taunt3D_buffactivate"
                        "Play_sfx_SkarnerBasicAttack2_OnCast"
                        "Play_sfx_SkarnerBasicAttack2_OnHit"
                        "Play_sfx_SkarnerBasicAttack_OnCast"
                        "Play_sfx_SkarnerBasicAttack_OnHit"
                        "Play_sfx_SkarnerCritAttack_OnCast"
                        "Play_sfx_SkarnerCritAttack_OnHit"
                        "Play_sfx_SkarnerE_OnCast"
                        "Play_sfx_SkarnerPassiveAttack_OnCast"
                        "Play_sfx_SkarnerPassiveAttack_OnHit"
                        "Play_sfx_SkarnerQ_OnCast"
                        "Play_sfx_SkarnerQClawAttack_OnCast"
                        "Play_sfx_SkarnerQClawAttack_OnHit"
                        "Play_sfx_SkarnerQRockAttack_OnCast"
                        "Play_sfx_SkarnerQRockAttack_OnHit"
                        "Play_sfx_SkarnerQRockThrow_OnCast"
                        "Play_sfx_SkarnerTurretAttack_OnCast"
                        "Play_sfx_SkarnerTurretAttack_OnHit"
                        "Stop_sfx_Skarner_E_warning_loop"
                        "Stop_sfx_Skarner_Q_OnCast"
                        "Stop_sfx_Skarner_QRockThrow_OnCast"
                        "Stop_sfx_Skarner_SkarnerEGrab_buffactivate"
                        "Stop_sfx_Skarner_SkarnerEMovement_footstep"
                        "Stop_sfx_Skarner_SkarnerEMovement_loop"
                        "Stop_sfx_Skarner_SkarnerP_loop"
                        "Stop_sfx_Skarner_SkarnerQ_timer"
                        "Stop_sfx_Skarner_SkarnerQThrow_missilelaunch"
                        "Stop_sfx_Skarner_SkarnerR_buffactivate"
                        "Stop_sfx_Skarner_SkarnerR_cast"
                        "Stop_sfx_Skarner_SkarnerR_hitlocation"
                        "Stop_sfx_Skarner_SkarnerW_cast"
                        "Stop_sfx_Skarner_SkarnerW_missilelaunch"
                    }
                }
                BankUnit {
                    Name: string = "Skarner_Base_SFX_OutOfGame"
                }
                BankUnit {
                    Name: string = "Skarner_Base_VO"
                    BankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Skarner/Skins/Base/Skarner_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Skarner/Skins/Base/Skarner_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Skarner/Skins/Base/Skarner_Base_VO_audio.wpk"
                    }
                    Events: list[string] = {
                        "Play_vo_Skarner_Attack2DBaron"
                        "Play_vo_Skarner_Attack2DBlueSentinel"
                        "Play_vo_Skarner_Attack2DElderDragon"
                        "Play_vo_Skarner_Attack2DElementalDragon"
                        "Play_vo_Skarner_Attack2DGeneral"
                        "Play_vo_Skarner_Attack2DGromp"
                        "Play_vo_Skarner_Attack2DHerald"
                        "Play_vo_Skarner_Attack2DKrug"
                        "Play_vo_Skarner_Attack2DNeutral"
                        "Play_vo_Skarner_Dance3DGeneral"
                        "Play_vo_Skarner_Dance5DGeneral"
                        "Play_vo_Skarner_Death3D"
                        "Play_vo_Skarner_Death5D"
                        "Play_vo_Skarner_FirstEncounter5DAscended"
                        "Play_vo_Skarner_FirstEncounter5DAzir"
                        "Play_vo_Skarner_FirstEncounter5DBelVeth"
                        "Play_vo_Skarner_FirstEncounter5DDarkin"
                        "Play_vo_Skarner_FirstEncounter5DGeneral"
                        "Play_vo_Skarner_FirstEncounter5DIxtal"
                        "Play_vo_Skarner_FirstEncounter5DJax"
                        "Play_vo_Skarner_FirstEncounter5DMalphite"
                        "Play_vo_Skarner_FirstEncounter5DMilio"
                        "Play_vo_Skarner_FirstEncounter5DQiyana"
                        "Play_vo_Skarner_FirstEncounter5DRammus"
                        "Play_vo_Skarner_FirstEncounter5DTaliyah"
                        "Play_vo_Skarner_FirstEncounter5DVoid"
                        "Play_vo_Skarner_FirstEncounter5DZyra"
                        "Play_vo_Skarner_Joke3DGeneral"
                        "Play_vo_Skarner_Joke5DGeneral"
                        "Play_vo_Skarner_JokeResponse3DGeneral"
                        "Play_vo_Skarner_JokeResponse5DGeneral"
                        "Play_vo_Skarner_Kill3DAscended"
                        "Play_vo_Skarner_Kill3DAzir"
                        "Play_vo_Skarner_Kill3DBelVeth"
                        "Play_vo_Skarner_Kill3DDarkin"
                        "Play_vo_Skarner_Kill3DGeneral"
                        "Play_vo_Skarner_Kill3DIxtal"
                        "Play_vo_Skarner_Kill3DJax"
                        "Play_vo_Skarner_Kill3DMalphite"
                        "Play_vo_Skarner_Kill3DMilio"
                        "Play_vo_Skarner_Kill3DPenta"
                        "Play_vo_Skarner_Kill3DQiyana"
                        "Play_vo_Skarner_Kill3DRammus"
                        "Play_vo_Skarner_Kill3DTaliyah"
                        "Play_vo_Skarner_Kill5DAscended"
                        "Play_vo_Skarner_Kill5DAzir"
                        "Play_vo_Skarner_Kill5DBelVeth"
                        "Play_vo_Skarner_Kill5DDarkin"
                        "Play_vo_Skarner_Kill5DGeneral"
                        "Play_vo_Skarner_Kill5DIxtal"
                        "Play_vo_Skarner_Kill5DJax"
                        "Play_vo_Skarner_Kill5DMalphite"
                        "Play_vo_Skarner_Kill5DMilio"
                        "Play_vo_Skarner_Kill5DPenta"
                        "Play_vo_Skarner_Kill5DQiyana"
                        "Play_vo_Skarner_Kill5DRammus"
                        "Play_vo_Skarner_Kill5DTaliyah"
                        "Play_vo_Skarner_Laugh3DGeneral"
                        "Play_vo_Skarner_Laugh5DGeneral"
                        "Play_vo_Skarner_Move2DFirst"
                        "Play_vo_Skarner_Move2DJungle"
                        "Play_vo_Skarner_Move2DLong"
                        "Play_vo_Skarner_Move2DStandard"
                        "Play_vo_Skarner_Recall5DGeneral"
                        "Play_vo_Skarner_Respawn2DGeneral"
                        "Play_vo_Skarner_SkarnerBasicAttack2_cast3D"
                        "Play_vo_Skarner_SkarnerBasicAttack2_cast5D"
                        "Play_vo_Skarner_SkarnerBasicAttack3_cast3D"
                        "Play_vo_Skarner_SkarnerBasicAttack3_cast5D"
                        "Play_vo_Skarner_SkarnerBasicAttack_cast3D"
                        "Play_vo_Skarner_SkarnerBasicAttack_cast5D"
                        "Play_vo_Skarner_SkarnerCritAttack_cast3D"
                        "Play_vo_Skarner_SkarnerCritAttack_cast5D"
                        "Play_vo_Skarner_SkarnerQ_cast3D"
                        "Play_vo_Skarner_SkarnerQ_cast5D"
                        "Play_vo_Skarner_SkarnerQClawAttack_cast3D"
                        "Play_vo_Skarner_SkarnerQClawAttack_cast5D"
                        "Play_vo_Skarner_SkarnerQRockAttack_cast3D"
                        "Play_vo_Skarner_SkarnerQRockAttack_cast5D"
                        "Play_vo_Skarner_SkarnerQRockThrow_cast3D"
                        "Play_vo_Skarner_SkarnerQRockThrow_cast5D"
                        "Play_vo_Skarner_SkarnerQRockThrow_hit3D"
                        "Play_vo_Skarner_SkarnerQRockThrow_hit5D"
                        "Play_vo_Skarner_SkarnerR_cast3D"
                        "Play_vo_Skarner_SkarnerR_cast5D"
                        "Play_vo_Skarner_SkarnerW_cast3D"
                        "Play_vo_Skarner_SkarnerW_cast5D"
                        "Play_vo_Skarner_Spell3DEStun"
                        "Play_vo_Skarner_Spell3DRHitMax"
                        "Play_vo_Skarner_Spell5DEStun"
                        "Play_vo_Skarner_Spell5DRHitMax"
                        "Play_vo_Skarner_Taunt3DGeneral"
                        "Play_vo_Skarner_Taunt5DGeneral"
                        "Play_vo_Skarner_TauntResponse3DGeneral"
                        "Play_vo_Skarner_TauntResponse5DGeneral"
                    }
                    VoiceOver: bool = true
                }
            }
        }
        SkinAnimationProperties: embed = SkinAnimationProperties {
            AnimationGraphData: link = "Characters/Skarner/Animations/Skin0"
        }
        SkinMeshProperties: embed = SkinMeshDataProperties {
            Skeleton: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Rework_Base.Skarner_Rework.skl"
            SimpleSkin: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Rework_Base.Skarner_Rework.skn"
            Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Mat_Body.dds"
            SkinScale: f32 = 0.899999976
            SelfIllumination: f32 = 0.699999988
            OverrideBoundingBox: option[vec3] = {
                { 280, 160, 280 }
            }
            Material: link = 0xeda67532
            InitialSubmeshToHide: string = "Stone"
            MaterialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Mat_Body.dds"
                    Submesh: string = "Mat_Body"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Mat_Mask.dds"
                    Submesh: string = "Mat_Mask"
                }
                SkinMeshDataProperties_MaterialOverride {
                    Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Mat_Mask.dds"
                    Submesh: string = "Stone"
                }
            }
            RigPoseModifierData: list[pointer] = {
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0xaf16cf46
                    mEndingJointName: hash = 0xae16cdb3
                    mDefaultMaskName: hash = 0x7136e1bc
                    mMaxBoneAngle: f32 = 20
                    mDampingValue: f32 = 5
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0xb8168555
                    mEndingJointName: hash = 0xb516809c
                    mDefaultMaskName: hash = 0x7136e1bc
                    mMaxBoneAngle: f32 = 24
                    mDampingValue: f32 = 6
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0x4a782e84
                    mEndingJointName: hash = 0x4d78333d
                    mDefaultMaskName: hash = 0x7136e1bc
                    mMaxBoneAngle: f32 = 22
                    mDampingValue: f32 = 4
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = 0xbdd959d1
                    mEndingJointName: hash = 0xb8168555
                    mDefaultMaskName: hash = 0x8a9731a7
                    mMaxBoneAngle: f32 = 25
                    mDampingValue: f32 = 5
                    mVelMultiplier: f32 = 0.5
                }
            }
        }
        ArmorMaterial: string = "Stone"
        DefaultAnimations: list[string] = {
            "Buffbones_Idle"
        }
        mContextualActionData: link = "Characters/Skarner/CAC/Skarner_Base"
        IconCircle: option[string] = {
            "ASSETS/Characters/Skarner/HUD/Skarner_Circle_0.Skarner_Rework.dds"
        }
        IconSquare: option[string] = {
            "ASSETS/Characters/Skarner/HUD/Skarner_Square_0.Skarner_Rework.dds"
        }
        HealthBarData: embed = CharacterHealthBarDataRecord {
            UnitHealthBarStyle: u8 = 10
        }
        mResourceResolver: link = "Characters/Skarner/Skins/Skin0/Resources"
    }
    0x05c64a70 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = 0x7de19a64
                        }
                    }
                    ChildrenProbability: embed = ValueFloat {
                        ConstantValue: f32 = 1
                    }
                }
                EmitterName: string = "Rock2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -100, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 3
                ParticleIsLocalOrientation: flag = true
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 60 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0.100000001, 0.300000012, 1.29999995 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.5
                        }
                        Values: list[vec3] = {
                            { 0, 0, -3.89999986 }
                            { 0, 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLingerType: u8 = 1
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterLinger: option[f32] = {
                    1
                }
                EmitterName: string = "firedome"
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -200, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_W_AirTrail07.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.600000024, 0.650980413, 0.588235319, 0.541176498 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.301500678
                            0.522415459
                            0.809696555
                            0.888217509
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.869163513 }
                            { 1, 1, 1, 0.179468185 }
                            { 1, 1, 1, 0.0833333358 }
                            { 0.9921875, 0.9921875, 0.9921875, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                AlphaRef: u8 = 0
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.575716257
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.621019125
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.300000012
                    ErosionFeatherOut: f32 = 0.300000012
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Wave02_01.Skarner_Rework.dds"
                    ErosionMapAddressMode: u8 = 0
                }
                DisableBackfaceCull: bool = true
                IsRotationEnabled: flag = true
                UvScrollClamp: flag = true
                IsFollowingTerrain: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 360, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 8, 12, 8 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.151912153
                            0.476035625
                            1.00497532
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.246254891, 0.701152444, 0.246254891 }
                            { 0.511802554, 1.23717976, 0.511802554 }
                            { 0.688493609, 1.74582303, 0.688493609 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Wave02_01.Skarner_Rework.dds"
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 3, 0.699999988 }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_W_Sheen2.Skarner_Rework.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    0x38123c47: flag = true
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLingerType: u8 = 1
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterLinger: option[f32] = {
                    1
                }
                EmitterName: string = "firedome1"
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -230, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_W_AirTrail07.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.600000024, 0.650980413, 0.588235319, 0.541176498 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.301500678
                            0.522415459
                            0.809696555
                            0.888217509
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.869163513 }
                            { 1, 1, 1, 0.179468185 }
                            { 1, 1, 1, 0.0833333358 }
                            { 0.9921875, 0.9921875, 0.9921875, 0 }
                        }
                    }
                }
                Pass: i16 = 50
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    BeginIn: f32 = 10
                    DeltaIn: f32 = 5
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.575716257
                                1
                            }
                            Values: list[f32] = {
                                0
                                0.621019125
                                1
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.300000012
                    ErosionFeatherOut: f32 = 0.300000012
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Wave02_01.Skarner_Rework.dds"
                    ErosionMapAddressMode: u8 = 0
                }
                DisableBackfaceCull: bool = true
                IsRotationEnabled: flag = true
                UvScrollClamp: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 360, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 8, 12, 8 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.151912153
                            0.476035625
                            1.00497532
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.246254891, 0.701152444, 0.246254891 }
                            { 0.511802554, 1.23717976, 0.511802554 }
                            { 0.688493609, 1.74582303, 0.688493609 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Wave02_01.Skarner_Rework.dds"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 2 }
                }
                ParticleUvScrollRate: embed = IntegratedValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_W_Sheen2.Skarner_Rework.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    0x38123c47: flag = true
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x538effa4: flag = true
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    0.699999988
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Big Boom"
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -800, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0172413792
                            0.313479632
                            1
                        }
                        Values: list[vec3] = {
                            { 0, -800, 0 }
                            { 0, -197.489532, 0 }
                            { 0, -190.794983, 0 }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_sk.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.60999465, 0.659998477, 0.600000024, 0.459998488 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.400000006 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 501
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 40
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                            Values: list[f32] = {
                                0.100000001
                                0.25
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionSliceWidth: f32 = 1
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_P_Erode.Skarner_Rework.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                DepthBiasFactors: vec2 = { 0, -80 }
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 360, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 90, 360, 0 }
                        }
                    }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 10 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 10 }
                            { 0, 0, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 2, 12 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.12309783
                            0.188858703
                            1
                        }
                        Values: list[vec3] = {
                            { 0.719999969, 0.719999969, 0.719999969 }
                            { 1.2270422, 1.2270422, 1.2270422 }
                            { 1.39690137, 1.38498187, 1.38498187 }
                            { 1.79999995, 1.79999995, 1.79999995 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Noise3.Skarner_Rework.dds"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.75, 0 }
                }
                TexDiv: vec2 = { 0.5, 1 }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.899999976, 1 }
                }
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 180
                }
            }
        }
        ParticleName: string = "Skarner_Base_Q_Mis_Rock"
        ParticlePath: string = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Q_Mis_Rock"
        SoundPersistentDefault: string = "Play_sfx_Skarner_SkarnerQThrow_missilelaunch"
        Flags: u16 = 212
    }
    0x48b34bd5 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1.79999995
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Basic5"
                0xa786282d: flag = true
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -25, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.510002315, 0.829999208, 0.76000613, 0.379995435 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            0.999000013
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -150
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                0x2bf854fb: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 180, 0, 90 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 220, 180, 0 }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Missile_Head_2.Skarner_Rework.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    3
                }
                IsSingleParticle: flag = true
                ChildParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    ChildrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            EffectKey: hash = 0xd893402a
                        }
                    }
                    ChildrenProbability: embed = ValueFloat {
                        ConstantValue: f32 = 1
                    }
                    ChildEmitOnDeath: bool = true
                }
                EmitterName: string = "Death_Child"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleIsLocalOrientation: flag = true
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Rock"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Rock.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 3
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.73571372, 0.73571372, 0.73571372, 1 }
                }
                Pass: i16 = -100
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 270 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -480, 0 }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Mat_Eye.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Dust_Ground"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 100, 800 }
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
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 100, 800 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 2, 8 }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 100, 100, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -40 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.429999232, 0.560006082, 0.549996197, 0.650003791 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.122257054
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 40, 20, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 40, 20, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 0 }
                            { 2, 2, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Smoke_Dust_White.Skarner_Rework.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.075000003
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLingerType: u8 = 2
                ParticleLinger: option[f32] = {
                    0.800000012
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Airwave_Close"
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 4, 0 }
                }
                Velocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -800, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0.0172413792
                            0.313479632
                            1
                        }
                        Values: list[vec3] = {
                            { 0, -800, 0 }
                            { 0, -197.489532, 0 }
                            { 0, -190.794983, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_W_Dune_1.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.611764729, 0.65882355, 0.600000024, 0.458823532 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.159060419
                            0.850000024
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.917647064, 0.917647064, 0.917647064, 1 }
                            { 0.274509817, 0.274509817, 0.274509817, 0 }
                        }
                    }
                }
                Pass: i16 = 1
                MeshRenderFlags: u8 = 0
                AlphaRef: u8 = 0
                SoftParticleParams: pointer = VfxSoftParticleDefinitionData {
                    DeltaIn: f32 = 30
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 4
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                1
                            }
                            Values: list[f32] = {
                                0
                                4
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.349999994
                    ErosionFeatherOut: f32 = 0.5
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Erosion.Skarner_Rework.dds"
                }
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10, 20, 10 }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.899999976, 1, 0.899999976 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.164765105
                            0.294966459
                            1
                        }
                        Values: list[vec3] = {
                            { 0.579836071, 0.644262314, 0.579836071 }
                            { 0.761325955, 0.846000016, 0.761325955 }
                            { 0.825116873, 0.916796565, 0.825116873 }
                            { 1.79999995, 2, 1.79999995 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_GradientV.Skarner_Rework.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.5 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 0.5 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 230
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                Lifetime: option[f32] = {
                    0.75
                }
                EmitterName: string = "Trail_Blend_"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {}
                Primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 800
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 500, 0, 0 }
                        }
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.701960802, 0.941176474, 0.90196079, 0.788235307 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec4] = {
                            { 0.701960802, 0.941176474, 0.90196079, 0 }
                            { 0.701960802, 0.941176474, 0.90196079, 0.788235307 }
                            { 0.701960802, 0.941176474, 0.90196079, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                            0.999899983
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.506218076, 0.506218076, 0.506218076, 0 }
                            { 0.314259559, 0.311253518, 0.311253518, 0 }
                        }
                    }
                }
                Pass: i16 = -50
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0.400000006
                                1
                            }
                            Values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    ErosionFeatherOut: f32 = 0.300000012
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Trail_Mult.Skarner_Rework.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                ParticleIsLocalOrientation: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 125, 80, 20 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1.20000005, 1.20000005, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/3026_Items_Trail_06.Skarner_Rework.dds"
                EmitterUvScrollRate: vec2 = { 1, 0 }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.5, 1 }
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                }
                ParticleLinger: option[f32] = {
                    0.100000001
                }
                Lifetime: option[f32] = {
                    0.75
                }
                EmitterName: string = "Trail_Blend_1"
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            ConstantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.701960802, 0.941176474, 0.90196079, 0.372549027 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec4] = {
                            { 0.701960802, 0.941176474, 0.90196079, 0 }
                            { 0.701960802, 0.941176474, 0.90196079, 0.372549027 }
                            { 0.701960802, 0.941176474, 0.90196079, 0 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.699999988
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.61351949, 0.61351949, 0.61351949, 0.501960814 }
                            { 0.348470271, 0.339467466, 0.339467466, 0 }
                            { 0.129411772, 0.0941176489, 0.0901960805, 0 }
                        }
                    }
                }
                Pass: i16 = -50
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/common_color-rampdown.Skarner_Rework.dds"
                }
                0x676949a1: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 125, 90, 50 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 1.20000005, 1.20000005, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Trail.Skarner_Rework.dds"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0, 1 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Rock_Fresnel"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Rock.Skarner_Rework.scb"
                        mSubmeshesToDraw: list[hash] = {
                            0xc81958fa
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.0699931309, 0.100007631, 0.100007631, 0.530006886 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.700007617, 0.940001547, 0.900007606, 0.220004573 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00157858152
                            0.0482644439
                            0.96754539
                            1
                        }
                        Values: list[vec4] = {
                            { 0.700007617, 0.940001547, 0.900007606, 0.220004573 }
                            { 0.700007617, 0.940001547, 0.900007606, 0.220004573 }
                            { 0.700007617, 0.940001547, 0.900007606, 0.220004573 }
                            { 0.700007617, 0.940001547, 0.900007606, 0 }
                        }
                    }
                }
                Pass: i16 = -85
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = -1
                    ReflectionFresnel: f32 = 0.100000001
                    ReflectionFresnelColor: vec4 = { 0, 0.2399939, 0.209994659, 0 }
                    Fresnel: f32 = 0.25
                    FresnelColor: vec4 = { 0.700007617, 0.940001547, 0.900007606, 0 }
                }
                DepthBiasFactors: vec2 = { -1, -9 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 270 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -480, 0 }
                }
                Texture: string = "ASSETS/Shared/Particles/Library/HitEffect/common_color-hold.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.349999994
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "Left"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, -300, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                EmissionMeshScale: f32 = 0.600000024
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 45, 100, -125 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.329411775, 0.308567941, 0.300999463, 0.501960814 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.329411775, 0.308567941, 0.300999463, 0 }
                            { 0.329411775, 0.296467245, 0.280932844, 0.501960814 }
                            { 0.207981557, 0.185140774, 0.172336951, 0.255901605 }
                            { 0.329411775, 0.263795346, 0.239619181, 0 }
                        }
                    }
                }
                Pass: i16 = -2
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
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Gradient.Skarner_Rework.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                MiscRenderFlags: u8 = 1
                IsRandomStartFrame: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -100, -150, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { -100, -150, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.699999988, 1, 0.200000003 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.699999988, 1, 0.200000003 }
                            { 0.420000017, 3, 0.200000003 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_GroundSmoke02.Skarner_Rework.dds"
                NumFrames: u16 = 2
                TexDiv: vec2 = { 1, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.349999994
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "Right"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { -150, -300, 0 }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 0, 0 }
                }
                EmissionMeshScale: f32 = 0.600000024
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { -45, 100, -125 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.329411775, 0.308567941, 0.300999463, 0.501960814 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        Values: list[vec4] = {
                            { 0.329411775, 0.308567941, 0.300999463, 0 }
                            { 0.329411775, 0.296467245, 0.280932844, 0.501960814 }
                            { 0.207981557, 0.185140774, 0.172336951, 0.255901605 }
                            { 0.0355021805, 0.0332557485, 0.0324400589, 0 }
                        }
                    }
                }
                Pass: i16 = -2
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
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Gradient.Skarner_Rework.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                MiscRenderFlags: u8 = 1
                IsRandomStartFrame: flag = true
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                }
                Rotation0: embed = IntegratedValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, -150, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    1.10000002
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, -150, 0 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.699999988, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.699999988, 1, 1 }
                            { 0.420000017, 3, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_GroundSmoke02.Skarner_Rework.dds"
                NumFrames: u16 = 2
                TexDiv: vec2 = { 1, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Energy_Flame_Alpha5"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 130, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Skin03_Q_mis_energyflame.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.659998477, 0.880003035, 0.829999208, 0.330006868 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                }
                                KeyValues: list[f32] = {
                                    2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec4] = {
                            { 0.659998477, 0.880003035, 0.829999208, 0.330006868 }
                        }
                    }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.682536066, 0.682536066, 0.682536066, 1 }
                }
                Pass: i16 = 40
                AlphaRef: u8 = 20
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 4, 2 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Skin03_Q_TrailMult.Skarner_Rework.tex"
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1.60000002, 0 }
                }
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.600000024, 1.20000005 }
                }
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 90
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Augment_ParasiticRelationship_2_shape.Skarner_Rework.tex"
                    UvRotationMult: embed = ValueFloat {
                        ConstantValue: f32 = 180
                    }
                    BirthUvoffsetMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, 0.200000003 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Energy_Flame_Alpha7"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 130, 0 }
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Skin03_Q_mis_energyflame.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.700007617, 0.940001547, 0.900007606, 0.790005326 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.700007617, 0.700007617, 0.700007617, 0.480003059 }
                }
                Pass: i16 = 35
                AlphaRef: u8 = 20
                DisableBackfaceCull: bool = true
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 90, 0 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 4, 2 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Augment_ParasiticRelationship_2_shape.Skarner_Rework.tex"
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0.5 }
                }
                UvRotation: embed = ValueFloat {
                    ConstantValue: f32 = 180
                }
                TextureMult: pointer = 0xb097c1bd {
                    TextureMult: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_R_Wave02_01.Skarner_Rework.dds"
                    UvScaleMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 2, 1 }
                    }
                    BirthUvScrollRateMult: embed = ValueVector2 {
                        ConstantValue: vec2 = { 0, -2.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "Rock1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_Q_Rock.Skarner_Rework.scb"
                    }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.274296165, 0.430304408, 0.404715031, 1 }
                }
                Pass: i16 = -90
                MiscRenderFlags: u8 = 1
                ParticleIsLocalOrientation: flag = true
                DoesCastShadow: flag = true
                IsRotationEnabled: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 270 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, -480, 0 }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/AurelionSol_Base_AOE_Shimmer_Mult.Skarner_Rework.dds"
                UvScale: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0.5 }
                }
            }
        }
        ParticleName: string = "Skarner_Base_Q_Mis_Rock_Child"
        ParticlePath: string = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Q_Mis_Rock_Child"
    }
    0x7592e736 = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = -1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "RockFresnel"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -0.00100000005, 0 }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xc81958fa
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.639993906, 0.970000744, 0.930006862, 0.149996191 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.981780708, 0.981780708, 0.981780708, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00157858152
                            0.0482644439
                            0.787124157
                            1
                        }
                        Values: list[vec4] = {
                            { 0.981780708, 0.981780708, 0.981780708, 1 }
                            { 0.981780708, 0.981780708, 0.981780708, 1 }
                            { 0.981780708, 0.981780708, 0.981780708, 1 }
                            { 0.981780708, 0.981780708, 0.981780708, 0 }
                        }
                    }
                }
                Pass: i16 = 40
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = -1
                    ReflectionOpacityGlancing: f32 = 0.300000012
                    ReflectionFresnel: f32 = 0.100000001
                    ReflectionFresnelColor: vec4 = { 0, 0.2399939, 0.209994659, 0 }
                    Fresnel: f32 = 0.25
                    FresnelColor: vec4 = { 0, 0.243137255, 0.211764708, 0 }
                }
                DepthBiasFactors: vec2 = { -1, -9 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                Texture: string = "ASSETS/Shared/Particles/Library/HitEffect/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_colorGrad_16.Skarner_Rework.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 1
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
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
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            1
                        }
                    }
                }
                ParticleLingerType: u8 = 1
                ParticleLinger: option[f32] = {
                    0.25
                }
                RateByVelocityFunction: embed = ValueVector2 {
                    ConstantValue: vec2 = { 0.0199999996, 0 }
                }
                EmitterName: string = "backing_burst"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 150, 150, 150 }
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
                                    0
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
                            { 150, 150, 150 }
                        }
                    }
                }
                BirthDrag: embed = ValueVector3 {
                    ConstantValue: vec3 = { 2, 2, 2 }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -60, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -60, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Size: vec3 = { 50, 0, 50 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, -50 }
                }
                BlendMode: u8 = 1
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.710002303, 0.570000768, 0.480003059, 0.500007629 }
                }
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.698130786, 0.698130786, 0.698130786, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00135869568
                            0.0785326213
                            0.57198596
                            0.785846889
                            0.890254378
                            0.997282624
                        }
                        Values: list[vec4] = {
                            { 0.690511525, 0.690511525, 0.690511525, 0 }
                            { 0.690511525, 0.690511525, 0.690511525, 0.989086211 }
                            { 0.690511525, 0.690511525, 0.690511525, 0.490196079 }
                            { 0.690511525, 0.690511525, 0.690511525, 0.220085204 }
                            { 0.690511525, 0.690511525, 0.690511525, 0.0901960805 }
                            { 0.690511525, 0.690511525, 0.690511525, 0 }
                        }
                    }
                }
                Pass: i16 = -75
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        ConstantValue: f32 = 0
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.147609144
                                1
                            }
                            Values: list[f32] = {
                                0
                                0
                                0
                            }
                        }
                    }
                    ErosionMapName: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Base_SmokeErode.Skarner_Rework.dds"
                    ErosionMapChannelMixer: embed = ValueColor {
                        ConstantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                IsGroundLayer: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 90, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 90, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 0, 0 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 1, 1 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_4x4Smoke_White.Skarner_Rework.tex"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
        }
        ParticleName: string = "Skarner_Base_Q_State_Rock"
        ParticlePath: string = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Q_State_Rock"
        OverrideScaleCap: option[f32] = {
            -1
        }
    }
    0xad2e1caf = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLingerType: u8 = 1
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "startFresnel_Add"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -0.00100000005, 0 }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xa346f9c3
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.110002287, 0.319996953, 0.179995418, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00157858152
                            0.156884342
                            0.801541328
                            0.861905754
                        }
                        Values: list[vec4] = {
                            { 0.110002287, 0.319996953, 0.179995418, 0 }
                            { 0.110002287, 0.319996953, 0.179995418, 0.0566037744 }
                            { 0.110002287, 0.319996953, 0.179995418, 0.207547173 }
                            { 0.110002287, 0.319996953, 0.179995418, 0 }
                        }
                    }
                }
                Pass: i16 = 41
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = -1
                    ReflectionOpacityGlancing: f32 = 0.300000012
                    ReflectionFresnel: f32 = 0.300000012
                    ReflectionFresnelColor: vec4 = { 0, 0.243137255, 0.211764708, 0 }
                    Fresnel: f32 = 0.25
                    FresnelColor: vec4 = { 0, 0.243137255, 0.211764708, 0 }
                }
                DepthBiasFactors: vec2 = { -1, -9 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                Texture: string = "ASSETS/Shared/Particles/Library/HitEffect/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_colorGrad_16.Skarner_Rework.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLingerType: u8 = 1
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "startFresnel_Add1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -0.00100000005, 0 }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xa346f9c3
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.109803922, 0.321568638, 0.180392161, 1 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00157858152
                            0.0736088753
                            0.123322807
                            0.680261552
                            0.804303229
                            0.8936674
                        }
                        Values: list[vec4] = {
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 1 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                        }
                    }
                }
                Pass: i16 = 41
                ReflectionDefinition: pointer = VfxReflectionDefinitionData {
                    ReflectionMapTexture: string = "ASSETS/Shared/Particles/Generic_White_Cubemap.SKINS_Lillia_Skin28.dds"
                    ReflectionOpacityDirect: f32 = -1
                    ReflectionOpacityGlancing: f32 = 0.300000012
                    ReflectionFresnel: f32 = 0.300000012
                    ReflectionFresnelColor: vec4 = { 0, 0.243137255, 0.211764708, 0 }
                    Fresnel: f32 = 0.25
                    FresnelColor: vec4 = { 0, 0.243137255, 0.211764708, 0 }
                }
                DepthBiasFactors: vec2 = { -1, -9 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                Texture: string = "ASSETS/Shared/Particles/Library/HitEffect/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_colorGrad_16.Skarner_Rework.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.0500000007
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.800000012
                }
                ParticleLingerType: u8 = 1
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "startFresnel_Add2"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, -0.00100000005, 0 }
                }
                Primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xa346f9c3
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                BlendMode: u8 = 4
                Color: embed = ValueColor {
                    ConstantValue: vec4 = { 0.109803922, 0.321568638, 0.180392161, 0.490196079 }
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0.00157858152
                            0.0736088753
                            0.123322807
                            0.680000007
                            0.804303229
                            0.8964293
                        }
                        Values: list[vec4] = {
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                            { 0.109803922, 0.321568638, 0.180392161, 0.490196079 }
                            { 0.109803922, 0.321568638, 0.180392161, 0 }
                        }
                    }
                }
                Pass: i16 = 41
                DepthBiasFactors: vec2 = { -1, -9 }
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
                IsUniformScale: flag = true
                Texture: string = "ASSETS/Shared/Particles/Library/HitEffect/common_color-hold.dds"
                PaletteDefinition: pointer = VfxPaletteDefinitionData {
                    PaletteTexture: string = "ASSETS/Characters/Skarner/Skins/Base/Particles/Skarner_Rework_Base_colorGrad_16.Skarner_Rework.dds"
                    PaletteSelector: embed = ValueVector3 {
                        ConstantValue: vec3 = { 2, 0, 0 }
                    }
                    PaletteCount: i32 = 16
                }
            }
        }
        ParticleName: string = "Skarner_Base_Q_Activate_Claws"
        ParticlePath: string = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Q_Activate_Claws"
        OverrideScaleCap: option[f32] = {
            -1
        }
    }
    0x1bd9b3f0 = StaticMaterialDef {
        Name: string = "Characters/Skarner/Skins/Skin0/Materials/Skarner_LeftClaw"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Color_Mask_Texture"
                TextureName: string = "ASSETS/Shared/Materials/black.Skarner_Rework.dds"
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Rework_Base_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "iridescentTex"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_Iridescent_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScrollTex"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_AdditiveScrollTexture_TX_CM.Skarner_Rework.tex"
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScroll_Mask"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_Main_IdleMask_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture2"
                TextureName: string = "ASSETS/Shared/Materials/black.Skarner_Rework.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "Exclude_Mask_from_TintColor_Value"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineColor"
                Value: vec4 = { 0, 0, 0, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineThickness"
                Value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineSoftness"
                Value: vec4 = { 0.100000001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexTile"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "IridescentControl"
                Value: vec4 = { 0.75, 0.239999995, 1.29999995, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_R"
            }
            StaticMaterialShaderParamDef {
                Name: string = "TintColor"
                Value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_R"
                Value: vec4 = { 0, 0.300007641, 0.250003815, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_R"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_G"
                Value: vec4 = { 0, 0.500007629, 0.400000006, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveStrength_G"
                Value: vec4 = { 5, 0, 0, 0 }
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
                Name: string = "EXCLUDE_MASK_FROM_TINTCOLOR"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_ON"
                On: bool = false
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
        DynamicMaterial: pointer = DynamicMaterialDef {
            Parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    Name: string = "AdditiveStrength_G"
                    Driver: pointer = SwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    Spell: hash = 0xa69258ba
                                }
                                mValue: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 4
                                }
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {}
                    }
                }
                DynamicMaterialParameterDef {
                    Name: string = "AdditiveStrength_R"
                    Driver: pointer = SwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    Spell: hash = 0xa69258ba
                                }
                                mValue: pointer = FloatLiteralMaterialDriver {
                                    mValue: f32 = 4
                                }
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {}
                    }
                }
            }
        }
    }
    0xeda67532 = StaticMaterialDef {
        Name: string = "Characters/Skarner/Skins/Skin0/Materials/Skarner_Body"
        SamplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Color_Mask_Texture"
                TextureName: string = "ASSETS/Shared/Materials/black.Skarner_Rework.dds"
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Rework_Base_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "iridescentTex"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_Iridescent_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScrollTex"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_AdditiveScrollTexture_TX_CM.Skarner_Rework.tex"
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "AdditiveScroll_Mask"
                TextureName: string = "ASSETS/Characters/Skarner/Skins/Base/Skarner_Base_Main_IdleMask_TX_CM.Skarner_Rework.tex"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                SamplerName: string = "Diffuse_Texture2"
                TextureName: string = "ASSETS/Shared/Materials/black.Skarner_Rework.dds"
                AddressU: u32 = 1
                AddressV: u32 = 1
                AddressW: u32 = 1
            }
        }
        ParamValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                Name: string = "Exclude_Mask_from_TintColor_Value"
                Value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineColor"
                Value: vec4 = { 0, 0, 0, 1 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineThickness"
                Value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "OutlineSoftness"
                Value: vec4 = { 0.100000001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexTile"
                Value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "IridescentControl"
                Value: vec4 = { 1, 0.5, 0.5, 0 }
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
                Value: vec4 = { 1, 1, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_R"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveTexScrollSpeed_G"
            }
            StaticMaterialShaderParamDef {
                Name: string = "AdditiveScroll_ColorTint_G"
                Value: vec4 = { 1, 1, 1, 0 }
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
                Name: string = "EXCLUDE_MASK_FROM_TINTCOLOR"
                On: bool = false
            }
            StaticMaterialSwitchDef {
                Name: string = "OUTLINE_ON"
                On: bool = false
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
    "Characters/Skarner/Skins/Skin0/Resources" = ResourceResolver {
        ResourceMap: map[hash,link] = {
            "Skarner_BA_tar_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_BA_tar_01"
            "Skarner_BA_tar_crit_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_BA_tar_crit_01"
            "Skarner_Emote_Dance_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Emote_Dance_01"
            "Skarner_Emote_Joke_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Emote_Joke_01"
            "Skarner_Emote_Taunt_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Emote_Taunt_01"
            "Skarner_idle_flame_L" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_idle_flame_L"
            "Skarner_idle_flame_R" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_idle_flame_R"
            "Skarner_Passive_attach" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_Passive_attach"
            "Skarner_R_cas_01" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_R_cas_01"
            "Skarner_R_cas_02" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_R_cas_02"
            "Skarner_R_cas_04" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_R_cas_04"
            0x82f21dbf = 0x81f36474
            0x553af1bf = 0xc87c79a4
            0x76e597f8 = 0x0c8af37d
            0xe14b6a81 = 0x17aff3cf
            0x00add3f0 = 0x5f9213b3
            0x04b9f917 = 0xcb6d0366
            0xec712cc2 = 0xd974eab5
            0x06f3d2c9 = 0xd7e879ca
            0xc990832c = 0xba5784ea
            0x33d596eb = 0xf1cd4216
            0x30b14e39 = 0xdeba1fec
            0x41be781a = 0xf41e39a7
            0xcae449a0 = 0xa7d568a3
            0x50265d41 = 0x10a99940
            0xae429b1f = 0x05c64a70
            0x8e6a0740 = 0xc1486e45
            0x77a9fca4 = 0x7592e736
            0x737b6b28 = 0x9c568d95
            0x4d403483 = 0x31f01e4c
            0x20815887 = 0x6e04ec23
            0xc3b02d78 = 0x7675f363
            0x2a2a3648 = 0x88ab4503
            0x17c4392d = 0x38229770
            0xc9090b58 = 0x9172ee3e
            0x1d1cd3a2 = 0xf8a5cf32
            0xcc956a12 = 0x68fb85f3
            0xf43aee5b = 0x9296b802
            0x88d5c0d6 = 0x70782ddd
            0xd39eb28b = 0xfc33b2d6
            0x87cb53e8 = 0xad2e1caf
            0x7de19a64 = 0x48b34bd5
            0xd893402a = 0x5f1576f7
            0xe2f79fd2 = 0x386c5a83
            0x9cefb707 = 0x5fa13da2
            0xf885be7e = 0x4796a3ef
            0xe1f79e3f = 0x396c5c16
            0xe0f79cac = 0x3a6c5da9
            0xb83cfef9 = 0xa50f8308
            0x59f804d5 = 0xeb7724a6
            0xe4b27fdc = 0x287fd673
            0xf9044993 = 0xa50f8308
            0xc318b582 = 0x6522bf73
            0x925535a3 = 0xbe9595a6
            0x09a55546 = 0xbb17cd9f
            0x42be79ad = 0xf31e3814
            0x9c419e56 = 0x49746f1a
            0x97fdc95a = 0x46254cdb
            0xe8056abb = 0x4464e78c
            0x8cb224ba = 0x1075d519
            0x649d9ca2 = 0xb93408df
            0x060d3ac1 = 0xa849ff1c
            0x41bc99ac = 0x485b7507
            0xe50385f7 = 0xb3fa0027
            0x6adf6a56 = 0xadb46ec1
            0xd3401807 = 0x5ecb1918
            0xa541e0f9 = 0x6cddb2b4
            0xcd5fa949 = 0x1e501fed
            0x3acabad0 = 0xe2c21267
            0x9e70c082 = 0x4d13e611
            0x23b8d2a2 = 0x20ac3a11
            "Skarner_BA_tar_crit_02" = "Characters/Skarner/Skins/Skin0/Particles/Skarner_Base_BA_tar_crit_02"
            0x5cbd45ac = 0x93570833
            0x4abec2d2 = 0x3f5aefd9
            0x4852d70a = 0x73e67fc3
        }
    }
}
