#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Yasuo/Spells/YasuoRArmorPen" = SpellObject {
        mScriptName: string = "YasuoRArmorPen"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoRArmorPen"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility" = AbilityObject {
        mRootSpell: link = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
        mChildSpells: list[link] = {
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2W"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2Wrapper"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3Mis"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3MisMinion"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3MisW"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3W"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3Wrapper"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQW"
        }
        mName: string = "YasuoQ1WrapperAbility"
        AbilityTraits: u32 = 2048
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3Mis" = SpellObject {
        mScriptName: string = "YasuoQ3Mis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mCoefficient: f32 = 1.20000005
            mAnimationName: string = "Spell1d"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                1100
                1100
                1100
                1100
                1100
                1100
                1100
            }
            CastRadius: list[f32] = {
                210
                210
                210
                210
                210
                210
                210
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 90
                MovementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "buffbone_glb_ground_loc"
                    mSpeed: f32 = 1200
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 1
            MissileSpeed: f32 = 1200
            mMissileEffectKey: hash = "Yasuo_Q_wind_mis"
            mLineWidth: f32 = 90
            bHaveHitBone: bool = true
            SelectionPriority: u32 = 2
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            true
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                90
                                90
                                90
                                90
                                90
                                90
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3MisW" = SpellObject {
        mScriptName: string = "YasuoQ3MisW"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQInstaCleave"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ" = SpellObject {
        mScriptName: string = "YasuoQ"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoQW"
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1A"
            mCastTime: f32 = 0.349999994
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                520
                520
                520
                520
                520
                520
                520
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 12
            MissileSpeed: f32 = 8700
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper" = SpellObject {
        mScriptName: string = "YasuoQ1Wrapper"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mSpellTags: list[string] = {
                "Trait_SwapsIntoImmobilizingCCSpell"
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "BaseDamage"
                    mValues: list[f32] = {
                        -5
                        20
                        45
                        70
                        95
                        120
                        145
                    }
                }
                SpellDataValue {
                    mName: string = "StabRange"
                    mValues: list[f32] = {
                        450
                        450
                        450
                        450
                        450
                        450
                        450
                    }
                }
                SpellDataValue {
                    mName: string = "TornadoRange"
                    mValues: list[f32] = {
                        1100
                        1100
                        1100
                        1100
                        1100
                        1100
                        1100
                    }
                }
                SpellDataValue {
                    mName: string = "Cooldown"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    mName: string = "StabWidth"
                    mValues: list[f32] = {
                        80
                        80
                        80
                        80
                        80
                        80
                        80
                    }
                }
                SpellDataValue {
                    mName: string = "SpinWidth"
                    mValues: list[f32] = {
                        260
                        260
                        260
                        260
                        260
                        260
                        260
                    }
                }
                SpellDataValue {
                    mName: string = "GatheringStormDuration"
                    mValues: list[f32] = {
                        6
                        6
                        6
                        6
                        6
                        6
                        6
                    }
                }
                SpellDataValue {
                    mName: string = "KnockUpDurationTOOLTIPONLY"
                    mValues: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "BaseDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mCoefficient: f32 = 1.04999995
                        }
                    }
                }
                "TotalDamageCrit" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "BaseDamage"
                        }
                        StatBySubPartCalculationPart {
                            mStat: u8 = 2
                            mSubpart: pointer = StatByCoefficientCalculationPart {
                                mStat: u8 = 8
                                mCoefficient: f32 = 0.933300018
                            }
                        }
                    }
                    mPrecision: i32 = 1
                }
            }
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q1.dds"
            }
            CooldownTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mIgnoreRangeCheck: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 55
            mFloatVarsDecimals: list[i32] = {
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "YasuoQ1Wrapper"
                    mFormat: link = 0x89fef2a8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_YasuoQ1Wrapper_Name"
                        "keySummary" = "Spell_YasuoQ1Wrapper_Summary"
                        "keyTooltip" = "Spell_YasuoQ1Wrapper_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                        "keyCooldown" = "Spell_YasuoQ1Wrapper_Cooldown"
                        "keyTooltipExtendedBelowLine" = "Spell_YasuoQ1Wrapper_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "BaseDamage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_Damage"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
        0x4048c61e: pointer = 0xf195e56b {
            0x450d68a0: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        0x88536426: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    0x77e5e41c: u32 = 16777216
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = 0x743703ff
                            }
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2Wrapper" = SpellObject {
        mScriptName: string = "YasuoQ2Wrapper"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mSpellTags: list[string] = {
                "Trait_SwapsIntoImmobilizingCCSpell"
            }
            mCoefficient: f32 = 1
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q2.dds"
            }
            CooldownTime: list[f32] = {
                4
                4
                4
                4
                4
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 55
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                0x375656dd: hash = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ3W"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3MisMinion" = SpellObject {
        mScriptName: string = "YasuoQ3MisMinion"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        66
                        132
                        231
                        308
                        440
                        540
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        2.75
                        3
                        3.25
                        3.5
                        3.75
                        4
                        4.25
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1.20000005
            mAnimationName: string = "Spell1d"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRadius: list[f32] = {
                210
                210
                210
                210
                210
                210
                210
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 100
                MovementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "buffbone_glb_ground_loc"
                    mSpeed: f32 = 1200
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 1
            MissileSpeed: f32 = 1200
            mMissileEffectKey: hash = "Yasuo_Q_wind_mis"
            mLineWidth: f32 = 100
            bHaveHitBone: bool = true
            SelectionPriority: u32 = 2
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            true
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                100
                                100
                                100
                                100
                                100
                                100
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3" = SpellObject {
        mScriptName: string = "YasuoQ3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1C"
            mCastTime: f32 = 0.349999994
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                520
                520
                520
                520
                520
                520
                520
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                0x375656dd: hash = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2" = SpellObject {
        mScriptName: string = "YasuoQ2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1B"
            mCastTime: f32 = 0.349999994
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                520
                520
                520
                520
                520
                520
                520
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 15
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                0x375656dd: hash = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1" = SpellObject {
        mScriptName: string = "YasuoQ1"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1A"
            mCastTime: f32 = 0.349999994
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                520
                520
                520
                520
                520
                520
                520
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 12
            MissileSpeed: f32 = 8700
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
            mClientData: embed = SpellDataResourceClient {
                0x375656dd: hash = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQW" = SpellObject {
        mScriptName: string = "YasuoQW"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoQW"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        20
                        20
                        45
                        70
                        95
                        120
                        145
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {
                    Value: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q1.dds"
            }
            CooldownTime: list[f32] = {
                6.5
                6
                5.5
                5
                4.5
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                3250
                3250
                3250
                3250
                3250
                3250
                3250
            }
            CastRangeDisplayOverride: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 55
            mFloatVarsDecimals: list[i32] = {
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
                -1
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3W" = SpellObject {
        mScriptName: string = "YasuoQ3W"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoQW"
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1d"
            mAnimationWinddownName: string = "Spell1_Fire"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q3.dds"
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q3.dds"
            }
            CooldownTime: list[f32] = {
                6.5
                6
                5.5
                5
                4.5
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            bIsToggleSpell: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                3250
                3250
                3250
                3250
                3250
                3250
                3250
            }
            CastRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            CastRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 90
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                90
                                90
                                90
                                90
                                90
                                90
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ3W"
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ2W" = SpellObject {
        mScriptName: string = "YasuoQ2W"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoQW"
            mCoefficient: f32 = 1
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q2.dds"
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q2.dds"
            }
            CooldownTime: list[f32] = {
                6.5
                6
                5.5
                5
                4.5
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                3250
                3250
                3250
                3250
                3250
                3250
                3250
            }
            CastRangeDisplayOverride: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 55
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                55
                                55
                                55
                                55
                                55
                                55
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ3Wrapper" = SpellObject {
        mScriptName: string = "YasuoQ3Wrapper"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mSpellTags: list[string] = {
                "Trait_ImmobilizingCCSpell"
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1d"
            mAnimationWinddownName: string = "Spell1_Fire"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q3.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            bIsToggleSpell: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            CastRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 90
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                0x375656dd: hash = "Characters/Yasuo/Spells/YasuoQ1WrapperAbility/YasuoQ1Wrapper"
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                90
                                90
                                90
                                90
                                90
                                90
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ3W"
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack" = SpellObject {
        mScriptName: string = "YasuoBasicAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack_First"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_hit_tar_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoIsInCombat" = SpellObject {
        mScriptName: string = "YasuoIsInCombat"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoRKnockUpComboTar" = SpellObject {
        mScriptName: string = "YasuoRKnockUpComboTar"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoRKnockUpComboTar"
        }
    }
    "Characters/Yasuo/Spells/YasuoSkin54Manager" = SpellObject {
        mScriptName: string = "YasuoSkin54Manager"
    }
    "Characters/Yasuo/Spells/YasuoCritMod" = SpellObject {
        mScriptName: string = "YasuoCritMod"
        mSpell: pointer = SpellDataResource {}
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoRSpellPassive" = SpellObject {
        mScriptName: string = "YasuoRSpellPassive"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveMSShieldOn" = SpellObject {
        mScriptName: string = "YasuoPassiveMSShieldOn"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 65
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        40
                        80
                        120
                        160
                        200
                        240
                        280
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        5
                        14
                        23
                        32
                        41
                        50
                        59
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.899999976
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Passive.dds"
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                800
                800
                800
                800
                800
                800
                800
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 3.48000002
            MissileSpeed: f32 = 20
            Mana: list[f32] = {
                70
                80
                90
                100
                110
                120
            }
            SelectionPriority: u32 = 2
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoPassiveMSShieldOn"
        }
    }
    "Characters/Yasuo/Spells/YasuoEDash" = SpellObject {
        mScriptName: string = "YasuoEDash"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 7183
            mAlternateName: string = "YasuoDashWrapper"
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_E.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mHitEffectOrientType: u32 = 2
            bHaveHitBone: bool = true
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoDashWrapper" = SpellObject {
        mScriptName: string = "YasuoDashWrapper"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoDashWrapper"
            mSpellTags: list[string] = {
                "PositiveEffect_MoveBlock"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        50
                        60
                        70
                        80
                        90
                        100
                        110
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        11
                        10
                        9
                        8
                        7
                        6
                        6
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0.5
                        0.5
                        0.400000006
                        0.300000012
                        0.200000003
                        0.100000001
                        0.100000001
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        12.5
                        15
                        17.5
                        20
                        22.5
                        25
                        27.5
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        20
                        20
                        20
                        20
                        20
                        20
                        20
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.600000024
            mCoefficient2: f32 = 0.600000024
            mAnimationName: string = "Channel"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_E.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            CastRange: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mFloatVarsDecimals: list[i32] = {
                1
                1
                0
                2
                2
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoDashWrapper"
        }
    }
    "Characters/Yasuo/Spells/YasuoAnimationManager" = SpellObject {
        mScriptName: string = "YasuoAnimationManager"
    }
    "Characters/Yasuo/Spells/YasuoRStun" = SpellObject {
        mScriptName: string = "YasuoRStun"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoRStun"
        }
    }
    "Characters/Yasuo/Spells/YasuoWindWallTimerMis1" = SpellObject {
        mScriptName: string = "YasuoWindWallTimerMis1"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 7183
            mAlternateName: string = "ZyraQFissure"
            mCoefficient2: f32 = 0.200000003
            mAnimationName: string = ""
            mImgIconName: list[string] = {
                "ASSETS/Spells/Icons2D/ZyraQ.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                8000
                8000
                8000
                8000
                8000
                8000
                8000
            }
            CastRangeDisplayOverride: list[f32] = {
                825
                825
                825
                825
                825
                825
                825
            }
            CastRadius: list[f32] = {
                220
                220
                220
                220
                220
                220
                220
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 85
                MovementComponent: pointer = FixedSpeedMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mStartBoneName: string = "root"
                    mProjectTargetToCastRange: bool = true
                    mSpeed: f32 = 2000
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 2000
            mMissileEffectName: string = "Zyra_Dummy_Controller.troy"
            mLineWidth: f32 = 85
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Area {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        TextureRadiusOverrideName: string = "ASSETS/Spells/Textures/AOE.dds"
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoEQComboSoundHit" = SpellObject {
        mScriptName: string = "YasuoEQComboSoundHit"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                0xa47810c1: list2[hash] = {
                    "Champion"
                }
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        15
                        30
                        45
                        60
                        0
                        0
                        15
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        20
                        30
                        0
                        0
                        10
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6
                        6
                        6
                        6
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mAnimationName: string = "Spell4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            CannotBeSuppressed: bool = true
            CanCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            CastRadius: list[f32] = {
                20
                20
                20
                20
                20
                20
                20
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 13
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_OlafRagnarok"
        }
    }
    "Characters/Yasuo/Spells/YasuoEAbility" = AbilityObject {
        mRootSpell: link = "Characters/Yasuo/Spells/YasuoEAbility/YasuoE"
        mChildSpells: list[link] = {
            "Characters/Yasuo/Spells/YasuoEAbility/YasuoE"
        }
        mName: string = "YasuoEAbility"
    }
    "Characters/Yasuo/Spells/YasuoEAbility/YasuoE" = SpellObject {
        mScriptName: string = "YasuoE"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mCastRequirementsTarget: list[pointer] = {
                HasBuffCastRequirement {
                    mInvertResult: bool = true
                    mBuffName: hash = 0xefb28843
                }
            }
            mSpellTags: list[string] = {
                "PositiveEffect_MoveBlock"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {}
                SpellEffectAmount {
                    Value: list[f32] = {
                        11
                        10
                        9
                        8
                        7
                        6
                        6
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0.5
                        0.5
                        0.400000006
                        0.300000012
                        0.200000003
                        0.100000001
                        0.100000001
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {
                    Value: list[f32] = {
                        750
                        750
                        750
                        750
                        750
                        750
                        750
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "MaxStacks"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    mName: string = "StackDuration"
                    mValues: list[f32] = {
                        5
                        5
                        5
                        5
                        5
                        5
                        5
                    }
                }
                SpellDataValue {
                    mName: string = "BaseDamage"
                    mValues: list[f32] = {
                        50
                        60
                        70
                        80
                        90
                        100
                        110
                    }
                }
            }
            0xfb56608c: map[hash,embed] = {
                0x497ae878 = SpellDataValueVector {
                    SpellDataValues: list[embed] = {
                        SpellDataValue {
                            mName: string = "BaseDamage"
                            mValues: list[f32] = {
                                60
                                75
                                90
                                105
                                120
                                135
                                150
                            }
                        }
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "TotalDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "BaseDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mCoefficient: f32 = 0.200000003
                        }
                        StatByCoefficientCalculationPart {
                            mCoefficient: f32 = 0.600000024
                        }
                    }
                }
                0xc3dc9adc = GameCalculationModified {
                    mMultiplier: pointer = ByCharLevelInterpolationCalculationPart {
                        mStartValue: f32 = 0.150000006
                        mEndValue: f32 = 0.25
                    }
                    mModifiedGameCalculation: hash = "TotalDamage"
                }
            }
            mAnimationName: string = "Channel"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_E.dds"
            }
            CooldownTime: list[f32] = {
                0.5
                0.5
                0.400000006
                0.300000012
                0.200000003
                0.100000001
                0.100000001
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            mDoesNotConsumeCooldown: bool = true
            CastRange: list[f32] = {
                475
                475
                475
                475
                475
                475
                475
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mFloatVarsDecimals: list[i32] = {
                1
                1
                0
                2
                2
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mSpellCooldownOrSealedQueueThreshold: option[f32] = {
                0.5
            }
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "YasuoE"
                    mFormat: link = 0x89fef2a8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_YasuoE_Name"
                        "keySummary" = "Spell_YasuoE_Summary"
                        "keyTooltip" = "Spell_YasuoE_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "BaseDamage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Effect%dAmount"
                                    TypeIndex: i32 = 2
                                    NameOverride: string = "Spell_ListType_PerUnitCooldown"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Effect%dAmount"
                                    TypeIndex: i32 = 3
                                    NameOverride: string = "Spell_ListType_Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoDashWrapper"
        }
        0x4048c61e: pointer = 0xf195e56b {
            0x450d68a0: u32 = 1
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        0x88536426: hash = "TotalDamage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    0x77e5e41c: u32 = 256
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            EffectValueCalculationPart {
                                mEffectIndex: i32 = 2
                            }
                        }
                    }
                }
                0xb09016f6 {
                    0x77e5e41c: u32 = 16777216
                    0x725bd4d5: pointer = GameCalculation {}
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveAbility" = AbilityObject {
        mRootSpell: link = "Characters/Yasuo/Spells/YasuoPassiveAbility/YasuoPassive"
        mChildSpells: list[link] = {
            "Characters/Yasuo/Spells/YasuoPassiveAbility/YasuoPassive"
        }
        mName: string = "YasuoPassiveAbility"
        mType: u8 = 3
    }
    "Characters/Yasuo/Spells/YasuoDashGhosted" = SpellObject {
        mScriptName: string = "YasuoDashGhosted"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoQDamage" = SpellObject {
        mScriptName: string = "YasuoQDamage"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQDamage"
        }
    }
    "Characters/Yasuo/Spells/YasuoRAbility" = AbilityObject {
        mRootSpell: link = "Characters/Yasuo/Spells/YasuoRAbility/YasuoR"
        mChildSpells: list[link] = {
            "Characters/Yasuo/Spells/YasuoRAbility/YasuoR"
        }
        0x86ddaddb: bool = true
        mName: string = "YasuoRAbility"
        mType: u8 = 2
        AbilityTraits: u32 = 2048
    }
    "Characters/Yasuo/Spells/YasuoDummySpell" = SpellObject {
        mScriptName: string = "YasuoDummySpell"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                0xa47810c1: list2[hash] = {
                    "Champion"
                }
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        15
                        30
                        45
                        60
                        0
                        0
                        15
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        20
                        30
                        0
                        0
                        10
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6
                        6
                        6
                        6
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mAnimationName: string = "Spell4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            CannotBeSuppressed: bool = true
            CanCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            mSpellRevealsChampion: bool = false
            CastRadius: list[f32] = {
                20
                20
                20
                20
                20
                20
                20
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 13
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_OlafRagnarok"
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallTrigger" = SpellObject {
        mScriptName: string = "YasuoWMovingWallTrigger"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoWAbility" = AbilityObject {
        mRootSpell: link = "Characters/Yasuo/Spells/YasuoWAbility/YasuoW"
        mChildSpells: list[link] = {
            "Characters/Yasuo/Spells/YasuoWAbility/YasuoW"
        }
        mName: string = "YasuoWAbility"
    }
    "Characters/Yasuo/Spells/YasuoDashScalar" = SpellObject {
        mScriptName: string = "YasuoDashScalar"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                0xa47810c1: list2[hash] = {
                    "Champion"
                }
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        15
                        30
                        45
                        60
                        0
                        0
                        15
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        20
                        30
                        0
                        0
                        10
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6
                        6
                        6
                        6
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mAnimationName: string = "Spell4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_E.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            CannotBeSuppressed: bool = true
            CanCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            CastRadius: list[f32] = {
                20
                20
                20
                20
                20
                20
                20
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 13
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoDashScalar"
        }
    }
    "Characters/Yasuo/Spells/YasuoRAbility/YasuoR" = SpellObject {
        mScriptName: string = "YasuoR"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mSpellTags: list[string] = {
                "Trait_Ultimate"
                "PositiveEffect_MoveBlock"
                "Trait_ImmobilizingCCSpell"
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "RBaseDamage"
                    mValues: list[f32] = {
                        50
                        200
                        350
                        500
                        650
                        800
                        950
                    }
                }
                SpellDataValue {
                    mName: string = "RPercentArmorPen"
                    mValues: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellDataValue {
                    mName: string = "RBuffDuration"
                    mValues: list[f32] = {
                        15
                        15
                        15
                        15
                        15
                        15
                        15
                    }
                }
                SpellDataValue {
                    mName: string = "RKnockupDuration"
                    mValues: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
                SpellDataValue {
                    mName: string = "RRadius"
                    mValues: list[f32] = {
                        400
                        400
                        400
                        400
                        400
                        400
                        400
                    }
                }
                SpellDataValue {
                    mName: string = "RCastSearchRadius"
                    mValues: list[f32] = {
                        1100
                        1100
                        1100
                        1100
                        1100
                        1100
                        1100
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "Damage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        NamedDataValueCalculationPart {
                            mDataValue: hash = "RBaseDamage"
                        }
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 2
                            mStatFormula: u8 = 2
                            mCoefficient: f32 = 1.5
                        }
                    }
                }
            }
            mAnimationName: string = "Spell4"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_R.dds"
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_R_Grey.dds"
            }
            CooldownTime: list[f32] = {
                105
                70
                50
                30
                30
                30
                30
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            bIsToggleSpell: bool = true
            mIgnoreRangeCheck: bool = true
            CastRange: list[f32] = {
                1400
                1400
                1400
                1400
                1400
                1400
                1400
            }
            CastRadius: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "YasuoR"
                    mFormat: link = 0x89fef2a8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_YasuoR_Name"
                        "keySummary" = "Spell_YasuoR_Summary"
                        "keyTooltip" = "Spell_YasuoR_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 3
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "RBaseDamage"
                                    TypeIndex: i32 = 1
                                    NameOverride: string = "Spell_ListType_Damage"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        TextureRadiusOverrideName: string = "ASSETS/Spells/Textures/AOE.dds"
                    }
                }
            }
        }
        0x4048c61e: pointer = 0xf195e56b {
            0x450d68a0: u32 = 0
            0x6d548702: pointer = GameCalculation {
                mFormulaParts: list[pointer] = {
                    0xf3cbe7b2 {
                        0x88536426: hash = "Damage"
                    }
                }
            }
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    0x77e5e41c: u32 = 16777216
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = 0x8e42de06
                            }
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveAbility/YasuoPassive" = SpellObject {
        mScriptName: string = "YasuoPassive"
        mSpell: pointer = SpellDataResource {
            mRequiredUnitTags: embed = ObjectTags {
                0xa47810c1: list2[hash] = {
                    "Champion"
                }
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "YasuoCritToAD"
                    mValues: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellDataValue {
                    mName: string = "CritChanceMultiplier"
                    mValues: list[f32] = {
                        1
                        1
                        1
                        1
                        1
                        1
                        1
                    }
                }
                SpellDataValue {
                    mName: string = "PercentCritDamageReduction"
                    mValues: list[f32] = {
                        -0.100000001
                        -0.100000001
                        -0.100000001
                        -0.100000001
                        -0.100000001
                        -0.100000001
                        -0.100000001
                    }
                }
                SpellDataValue {
                    mName: string = "CherryShieldAmp"
                    mValues: list[f32] = {
                        1.29999995
                        1.29999995
                        1.29999995
                        1.29999995
                        1.29999995
                        1.29999995
                        1.29999995
                    }
                }
            }
            mSpellCalculations: map[hash,pointer] = {
                "ShieldValue" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelInterpolationCalculationPart {
                            mStartValue: f32 = 125
                            mEndValue: f32 = 600
                            0x7fe8e3b3: bool = true
                        }
                    }
                }
                0x74ce5438 = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        ByCharLevelBreakpointsCalculationPart {
                            mLevel1Value: f32 = 55
                            mBreakpoints: list[embed] = {
                                Breakpoint {
                                    mLevel: u32 = 7
                                    0xd5fd07ed: f32 = -5
                                }
                                Breakpoint {
                                    mLevel: u32 = 13
                                    0xd5fd07ed: f32 = -5
                                }
                                Breakpoint {
                                    mLevel: u32 = 19
                                    0xd5fd07ed: f32 = -5
                                }
                                Breakpoint {
                                    mLevel: u32 = 25
                                    0xd5fd07ed: f32 = -5
                                }
                            }
                        }
                    }
                }
                "CurrentCritDamage" = GameCalculation {
                    mFormulaParts: list[pointer] = {
                        StatByCoefficientCalculationPart {
                            mStat: u8 = 8
                            mCoefficient: f32 = 1
                        }
                    }
                    mDisplayAsPercent: bool = true
                    mPrecision: i32 = 1
                }
            }
            mCoefficient: f32 = 0.649999976
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Passive.dds"
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastConeAngle: f32 = 0
            CastConeDistance: f32 = 0
            MissileSpeed: f32 = 1200
            mLookAtPolicy: u32 = 0
            mHitEffectOrientType: u32 = 0
            mHitBoneName: string = "C_BUFFBONE_GLB_HEAD_LOC"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "YasuoPassive"
                    mFormat: link = 0x0b8004bb
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_YasuoPassive_Name"
                        "keySummary" = "Spell_YasuoPassive_Summary"
                        "keyTooltip" = "Spell_YasuoPassive_Tooltip"
                        "keyTooltipExtended" = "Spell_YasuoPassive_TooltipExtended"
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoPassive"
        }
    }
    "Characters/Yasuo/Spells/YasuoWChildMis" = SpellObject {
        mScriptName: string = "YasuoWChildMis"
        mSpell: pointer = SpellDataResource {
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                ""
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -1
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            AlwaysSnapFacing: bool = true
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mIgnoreRangeCheck: bool = true
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 7.5
            mLookAtPolicy: u32 = 1
            mHitEffectOrientType: u32 = 0
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionWall {
                        CenterLocator: embed = DrawablePositionLocator {
                            DistanceOffset: f32 = 300
                            OrientationType: u32 = 3
                        }
                        Thickness: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                100
                                100
                                100
                                100
                                100
                                100
                            }
                            mValueType: u32 = 2
                        }
                        Length: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                380
                                460
                                530
                                600
                                680
                                760
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQSound" = SpellObject {
        mScriptName: string = "YasuoQSound"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoWindWallBuff" = SpellObject {
        mScriptName: string = "YasuoWindWallBuff"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoCritAttack5" = SpellObject {
        mScriptName: string = "YasuoCritAttack5"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack_first"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectName: string = "Yasuo_basic_attack_hit_tar_1.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoCritAttack4" = SpellObject {
        mScriptName: string = "YasuoCritAttack4"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_Crit_hit_04"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoNotInCombat" = SpellObject {
        mScriptName: string = "YasuoNotInCombat"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack5" = SpellObject {
        mScriptName: string = "YasuoBasicAttack5"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack_first"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectName: string = "Yasuo_basic_attack_hit_tar_1.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack4" = SpellObject {
        mScriptName: string = "YasuoBasicAttack4"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_hit_tar_04"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack6" = SpellObject {
        mScriptName: string = "YasuoBasicAttack6"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack3"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectName: string = "Aatrox_basic_hit_effect_01.troy"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoCritAttack3" = SpellObject {
        mScriptName: string = "YasuoCritAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "DianaBasicAttack3"
            mAnimationName: string = "Attack3"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_Crit_hit_03"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoCritAttack2" = SpellObject {
        mScriptName: string = "YasuoCritAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "DianaBasicAttack2"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_Crit_hit_02"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack3" = SpellObject {
        mScriptName: string = "YasuoBasicAttack3"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "DianaBasicAttack3"
            mAnimationName: string = "Attack3"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_hit_tar_03"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoBasicAttack2" = SpellObject {
        mScriptName: string = "YasuoBasicAttack2"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "DianaBasicAttack2"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            mApplyMaterialOnHitSound: bool = true
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_hit_tar_02"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQProtect" = SpellObject {
        mScriptName: string = "YasuoQProtect"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoW_VisualMis" = SpellObject {
        mScriptName: string = "YasuoW_VisualMis"
        mSpell: pointer = SpellDataResource {
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                ""
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -1
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            AlwaysSnapFacing: bool = true
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mIgnoreRangeCheck: bool = true
            CastRange: list[f32] = {
                25000
                25000
                25000
                25000
                25000
                25000
                25000
            }
            CastRangeDisplayOverride: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 7.5
            mLookAtPolicy: u32 = 1
            mHitEffectOrientType: u32 = 0
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionWall {
                        CenterLocator: embed = DrawablePositionLocator {
                            DistanceOffset: f32 = 300
                            OrientationType: u32 = 3
                        }
                        Thickness: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                100
                                100
                                100
                                100
                                100
                                100
                            }
                            mValueType: u32 = 2
                        }
                        Length: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                380
                                460
                                530
                                600
                                680
                                760
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRSound4" = SpellObject {
        mScriptName: string = "YasuoRSound4"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveCounter" = SpellObject {
        mScriptName: string = "YasuoPassiveCounter"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoPassiveMSCharge"
        }
    }
    "Characters/Yasuo/Spells/YasuoRIsAvailable" = SpellObject {
        mScriptName: string = "YasuoRIsAvailable"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoRSound0" = SpellObject {
        mScriptName: string = "YasuoRSound0"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoRSound1" = SpellObject {
        mScriptName: string = "YasuoRSound1"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoRSound2" = SpellObject {
        mScriptName: string = "YasuoRSound2"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoCritAttack" = SpellObject {
        mScriptName: string = "YasuoCritAttack"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 5327
            mAlternateName: string = "GarenBasicAttack"
            mAnimationName: string = "Attack_First"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.367799997
            bHaveHitEffect: bool = true
            CastRange: list[f32] = {
                200
                200
                200
                200
                200
                200
                200
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 8
            MissileSpeed: f32 = 347.799988
            mHitEffectOrientType: u32 = 2
            mHitEffectKey: hash = "Yasuo_BA_Crit_hit_01"
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRSound3" = SpellObject {
        mScriptName: string = "YasuoRSound3"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveMSCharge" = SpellObject {
        mScriptName: string = "YasuoPassiveMSCharge"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoPassiveMSCharge"
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallMisOld" = SpellObject {
        mScriptName: string = "YasuoWMovingWallMisOld"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6152
            mAlternateName: string = "YasuoWMovingWall"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRange: list[f32] = {
                1200
                1200
                1200
                1200
                1200
                1200
                1200
            }
            CastRadius: list[f32] = {
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -300
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 550
                    mInitialSpeed: f32 = 550
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 15.0749998
            MissileSpeed: f32 = 550
            mMissileEffectKey: hash = "Yasuo_Wall_XinZhao_OLD"
            mLineWidth: f32 = 1
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallMisVis" = SpellObject {
        mScriptName: string = "YasuoWMovingWallMisVis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6152
            mAlternateName: string = "YasuoWMovingWall"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRange: list[f32] = {
                1200
                1200
                1200
                1200
                1200
                1200
                1200
            }
            CastRadius: list[f32] = {
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 15.0749998
            MissileSpeed: f32 = 850
            mMissileEffectName: string = "zyradummycontroller.troy"
            mLineWidth: f32 = 1
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoQE3" = SpellObject {
        mScriptName: string = "YasuoQE3"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 8192
            mCoefficient: f32 = 1
            mAnimationName: string = ""
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            mDoNotNeedToFaceTarget: bool = true
            CastRange: list[f32] = {
                260
                260
                260
                260
                260
                260
                260
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 12
            MissileSpeed: f32 = 8700
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
    }
    "Characters/Yasuo/Spells/YasuoQE2" = SpellObject {
        mScriptName: string = "YasuoQE2"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 8192
            mCoefficient: f32 = 1
            mAnimationName: string = ""
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            mDoNotNeedToFaceTarget: bool = true
            CastRange: list[f32] = {
                260
                260
                260
                260
                260
                260
                260
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 12
            MissileSpeed: f32 = 8700
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
    }
    "Characters/Yasuo/Spells/YasuoQE1" = SpellObject {
        mScriptName: string = "YasuoQE1"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 8192
            mCoefficient: f32 = 1
            mAnimationName: string = ""
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            mDoNotNeedToFaceTarget: bool = true
            CastRange: list[f32] = {
                260
                260
                260
                260
                260
                260
                260
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 12
            MissileSpeed: f32 = 8700
            mLineWidth: f32 = 15
            bHaveHitBone: bool = true
            mHitBoneName: string = "root"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ"
        }
    }
    "Characters/Yasuo/Spells/YasuoEQComboAnimLock" = SpellObject {
        mScriptName: string = "YasuoEQComboAnimLock"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveShield" = SpellObject {
        mScriptName: string = "YasuoPassiveShield"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 65
            mCoefficient: f32 = 0.899999976
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Passive.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 3.48000002
            MissileSpeed: f32 = 20
            SelectionPriority: u32 = 2
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {}
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoPassiveMSShieldOn"
        }
    }
    "Characters/Yasuo/Spells/YasuoRDummySpell" = SpellObject {
        mScriptName: string = "YasuoRDummySpell"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 20
            mAffectsTypeFlags: u32 = 9221
            mRequiredUnitTags: embed = ObjectTags {
                0xa47810c1: list2[hash] = {
                    "Champion"
                }
            }
            mSpellTags: list[string] = {
                "Trait_Ultimate"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        15
                        30
                        45
                        60
                        0
                        0
                        15
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        20
                        30
                        0
                        0
                        10
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6
                        6
                        6
                        6
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mAnimationName: string = "Spell4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            CannotBeSuppressed: bool = true
            CanCastWhileDisabled: bool = true
            mCantCancelWhileWindingUp: bool = true
            CastRadius: list[f32] = {
                20
                20
                20
                20
                20
                20
                20
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 13
            mTargetingTypeData: pointer = Self {}
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_OlafRagnarok"
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWall" = SpellObject {
        mScriptName: string = "YasuoWMovingWall"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 23759
            mAlternateName: string = "YasuoWMovingWall"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        10
                        15
                        20
                        25
                        30
                        35
                        40
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        60
                        90
                        120
                        150
                        180
                        210
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        3
                        6
                        9
                        12
                        15
                        18
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        250
                        300
                        350
                        400
                        450
                        500
                        550
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        250
                        320
                        390
                        460
                        530
                        600
                        670
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "WallLife"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
            }
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_W.dds"
            }
            mCastTime: f32 = 0.0125000002
            CooldownTime: list[f32] = {
                28
                26
                24
                22
                20
                18
                18
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            CastRange: list[f32] = {
                6000
                6000
                6000
                6000
                6000
                6000
                6000
            }
            CastRangeDisplayOverride: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastFrame: f32 = 7.5
            mLookAtPolicy: u32 = 1
            mTargetingTypeData: pointer = Direction {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionWall {
                        CenterLocator: embed = DrawablePositionLocator {
                            DistanceOffset: f32 = 300
                            OrientationType: u32 = 3
                        }
                        Thickness: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                100
                                100
                                100
                                100
                                100
                                100
                            }
                            mValueType: u32 = 2
                        }
                        Length: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                380
                                460
                                530
                                600
                                680
                                760
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRKnockUpComboW" = SpellObject {
        mScriptName: string = "YasuoRKnockUpComboW"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoRKnockUpComboW"
            mSpellTags: list[string] = {
                "Trait_Ultimate"
                "PositiveEffect_MoveBlock"
            }
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        200
                        300
                        400
                        100
                        130
                        0
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        33
                        66
                        100
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        650
                        750
                        850
                        950
                        1050
                        0
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        50
                        50
                        50
                        50
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        33
                        66
                        100
                        0
                        0
                        0
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1.5
            mCoefficient2: f32 = 0.600000024
            mAnimationName: string = "Channel"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_R.dds"
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_R_Grey.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                6
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            bIsToggleSpell: bool = true
            CastRange: list[f32] = {
                1400
                1400
                1400
                1400
                1400
                1400
                1400
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Area {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        OverrideRadius: embed = FloatPerSpellLevel {
                            mValueType: u32 = 1
                        }
                        TextureRadiusOverrideName: string = "ASSETS/Spells/Textures/AOE.dds"
                    }
                }
                mCustomTargeterDefinitions: map[hash,embed] = {
                    0x90c62908 = CustomTargeterDefinitions {
                        mTargeterDefinitions: list[pointer] = {
                            TargeterDefinitionAoe {
                                OverrideRadius: embed = FloatPerSpellLevel {
                                    mPerLevelValues: list[f32] = {
                                        800
                                        800
                                        800
                                        800
                                        800
                                        800
                                    }
                                }
                                TextureRadiusOverrideName: string = "ASSETS/Spells/Textures/AOE.dds"
                            }
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRAvailableTest" = SpellObject {
        mScriptName: string = "YasuoRAvailableTest"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallMisR" = SpellObject {
        mScriptName: string = "YasuoWMovingWallMisR"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6152
            mAlternateName: string = "VolleyAttack"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRange: list[f32] = {
                1200
                1200
                1200
                1200
                1200
                1200
                1200
            }
            CastRadius: list[f32] = {
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 15.0749998
            MissileSpeed: f32 = 850
            mMissileEffectName: string = "Zyra_Dummy_Controller.troy"
            mLineWidth: f32 = 1
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoDashWrapperChaos" = SpellObject {
        mScriptName: string = "YasuoDashWrapperChaos"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoDashWrapperChaos"
        }
    }
    0xdc3a3a15 = SpellObject {
        mScriptName: string = "YasuoQ3WAutoSmartCast"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 36
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoQW"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        25
                        40
                        55
                        70
                        85
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        85
                        90
                        95
                        100
                        105
                        110
                        115
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        75
                        85
                        95
                        105
                        115
                        125
                        135
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6.5
                        6
                        5.5
                        5
                        4.5
                        4
                        3.5
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1
            mAnimationName: string = "Spell1d"
            mAnimationWinddownName: string = "Spell1_Fire"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q3.dds"
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Q3.dds"
            }
            CooldownTime: list[f32] = {
                6.5
                6
                5.5
                5
                4.5
                4
                4
            }
            DelayCastOffsetPercent: f32 = -0.75
            DelayTotalTimePercent: f32 = -0.75
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            bIsToggleSpell: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mUseAutoattackCastTimeData: pointer = UseAutoattackCastTimeData {}
            CastRange: list[f32] = {
                3250
                3250
                3250
                3250
                3250
                3250
                3250
            }
            CastRangeDisplayOverride: list[f32] = {
                1000
                1000
                1000
                1000
                1000
                1000
                1000
            }
            CastRadius: list[f32] = {
                300
                300
                300
                300
                300
                300
                300
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 1500
            mLineWidth: f32 = 90
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            0x00f7e5bc: bool = true
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                90
                                90
                                90
                                90
                                90
                                90
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_YasuoQ3Open"
        }
    }
    "Characters/Yasuo/Spells/YasuoEQCombo" = SpellObject {
        mScriptName: string = "YasuoEQCombo"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "DariusCleave"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        50
                        50
                        50
                        50
                        50
                        50
                        50
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        35
                        70
                        105
                        140
                        175
                        210
                        245
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 1.04999995
            mCoefficient2: f32 = 0.699999988
            mAnimationName: string = "Spell3b"
            mCastTime: f32 = 0.234400004
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                270
                270
                270
                270
                270
                270
                270
            }
            CastRangeDisplayOverride: list[f32] = {
                1
                1
                1
                1
                1
                1
                1
            }
            CastRadiusSecondary: list[f32] = {
                425
                425
                425
                425
                425
                425
                425
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 0
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = SelfAoe {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionAoe {
                        CenterLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 1
                        }
                        OverrideRadius: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                425
                                425
                                425
                                425
                                425
                                425
                            }
                            mValueType: u32 = 2
                        }
                        TextureRadiusOverrideName: string = "ASSETS/Spells/Textures/darius_cleave_outside.dds"
                    }
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallMisL" = SpellObject {
        mScriptName: string = "YasuoWMovingWallMisL"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6152
            mAlternateName: string = "VolleyAttack"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRange: list[f32] = {
                1800
                1800
                1800
                1800
                1800
                1800
                1800
            }
            CastRadius: list[f32] = {
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 15.0749998
            MissileSpeed: f32 = 850
            mMissileEffectName: string = "Zyra_Dummy_Controller.troy"
            mLineWidth: f32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoDash" = SpellObject {
        mScriptName: string = "YasuoDash"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "YasuoDashWrapper"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        10
                        40
                        70
                        100
                        130
                        160
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {
                    Value: list[f32] = {
                        550
                        650
                        750
                        850
                        950
                        1050
                        1150
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.600000024
            mCoefficient2: f32 = 0.600000024
            mAnimationName: string = "Spell3"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_E.dds"
            }
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            mSpellRevealsChampion: bool = false
            CastRange: list[f32] = {
                550
                550
                550
                550
                550
                550
                550
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 9
            MissileSpeed: f32 = 20
            mHitEffectOrientType: u32 = 2
            bHaveHitBone: bool = true
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRLeashParticle" = SpellObject {
        mScriptName: string = "YasuoRLeashParticle"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallEnemy" = SpellObject {
        mScriptName: string = "YasuoWMovingWallEnemy"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 23759
            mAlternateName: string = "YasuoWMovingWall"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        10
                        15
                        20
                        25
                        30
                        35
                        40
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        60
                        90
                        120
                        150
                        180
                        210
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        7
                        7
                        7
                        7
                        7
                        7
                        7
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.800000012
            mAnimationName: string = "Spell2"
            mCastTime: f32 = 0.0125000002
            CooldownTime: list[f32] = {
                29
                26
                23
                20
                17
                13
                13
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            CastRange: list[f32] = {
                600
                600
                600
                600
                600
                600
                600
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastConeAngle: f32 = 22.3199997
            CastConeDistance: f32 = 650
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 902
            mLookAtPolicy: u32 = 1
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            mTargetingTypeData: pointer = Cone {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionCone {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        ConeAngleDegrees: option[f32] = {
                            22.3199997
                        }
                        ConeRange: option[f32] = {
                            650
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoPassiveMovementShield" = SpellObject {
        mScriptName: string = "YasuoPassiveMovementShield"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_ItemStatikkShank"
        }
    }
    "Characters/Yasuo/Spells/YasuoRKnockUpCombo" = SpellObject {
        mScriptName: string = "YasuoRKnockUpCombo"
        mSpell: pointer = SpellDataResource {
            Flags: u32 = 4
            mAffectsTypeFlags: u32 = 23615
            mAffectsStatusFlags: u32 = 16
            mAlternateName: string = "YasuoRKnockUpComboW"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        35
                        60
                        85
                        110
                        135
                        160
                        185
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        15
                        15
                        15
                        15
                        15
                        15
                        15
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                        1.5
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        80
                        80
                        55
                        30
                        30
                        30
                        30
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.400000006
            mAnimationName: string = "Spell4"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.5
            DelayTotalTimePercent: f32 = -0.5
            mCantCancelWhileWindingUp: bool = true
            CantCastWhileRooted: bool = true
            CastRange: list[f32] = {
                2500
                2500
                2500
                2500
                2500
                2500
                2500
            }
            CastRadius: list[f32] = {
                210
                210
                210
                210
                210
                210
                210
            }
            CastConeDistance: f32 = 100
            CastFrame: f32 = 25.8500004
            MissileSpeed: f32 = 0
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoR_TeleportVFX_Mis" = SpellObject {
        mScriptName: string = "YasuoR_TeleportVFX_Mis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAnimationName: string = ""
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            DelayCastOffsetPercent: f32 = -0.649999976
            DelayTotalTimePercent: f32 = -0.649999976
            mCantCancelWhileWindingUp: bool = true
            CastRange: list[f32] = {
                2600
                2600
                2600
                2600
                2600
                2600
                2600
            }
            CastRadius: list[f32] = {
                171.899994
                171.899994
                171.899994
                171.899994
                171.899994
                171.899994
                171.899994
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = "R_hand"
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 9.52000046
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Yasuo_R_dash"
            SelectionPriority: u32 = 2
            mTargetingTypeData: pointer = TargetOrLocation {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_AkaliMota"
        }
    }
    "Characters/Yasuo/Spells/YasuoWTrueCast" = SpellObject {
        mScriptName: string = "YasuoWTrueCast"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    "Characters/Yasuo/Spells/YasuoWAbility/YasuoW" = SpellObject {
        mScriptName: string = "YasuoW"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 23759
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        10
                        15
                        20
                        25
                        30
                        35
                        40
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        30
                        60
                        90
                        120
                        150
                        180
                        210
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        3
                        6
                        9
                        12
                        15
                        18
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        250
                        300
                        350
                        400
                        450
                        500
                        550
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        250
                        320
                        390
                        460
                        530
                        600
                        670
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mDataValues: list[embed] = {
                SpellDataValue {
                    mName: string = "WallLife"
                    mValues: list[f32] = {
                        4
                        4
                        4
                        4
                        4
                        4
                        4
                    }
                }
                SpellDataValue {
                    mName: string = "Width"
                    mValues: list[f32] = {
                        250
                        320
                        390
                        460
                        530
                        600
                        670
                    }
                }
                SpellDataValue {
                    mName: string = "TravelRange"
                    mValues: list[f32] = {
                        450
                        450
                        450
                        450
                        450
                        450
                        450
                    }
                }
                SpellDataValue {
                    mName: string = "BubbleRadius"
                    mValues: list[f32] = {
                        300
                        300
                        300
                        300
                        300
                        300
                        300
                    }
                }
                SpellDataValue {
                    mName: string = "Thickness"
                    mValues: list[f32] = {
                        100
                        100
                        100
                        100
                        100
                        100
                        100
                    }
                }
            }
            mAnimationName: string = "Spell2"
            mImgIconName: list[string] = {
                "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_W.dds"
            }
            mCastTime: f32 = 0.0130000003
            CooldownTime: list[f32] = {
                27
                25
                23
                21
                19
                17
                15
            }
            DelayCastOffsetPercent: f32 = -1
            DelayTotalTimePercent: f32 = -1
            mCantCancelWhileWindingUp: bool = true
            mProjectTargetToCastRange: bool = true
            AlwaysSnapFacing: bool = true
            UseAnimatorFramerate: bool = true
            mDoNotNeedToFaceTarget: bool = true
            mIgnoreRangeCheck: bool = true
            CastRange: list[f32] = {
                5000
                5000
                5000
                5000
                5000
                5000
                5000
            }
            CastRangeDisplayOverride: list[f32] = {
                400
                400
                400
                400
                400
                400
                400
            }
            CastRadius: list[f32] = {
                100
                100
                100
                100
                100
                100
                100
            }
            CastFrame: f32 = 7.5
            mLookAtPolicy: u32 = 1
            mHitEffectOrientType: u32 = 0
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTooltipData: pointer = TooltipInstanceSpell {
                    mObjectName: string = "YasuoW"
                    mFormat: link = 0x89fef2a8
                    mLocKeys: map[string,string] = {
                        "keyName" = "Spell_YasuoW_Name"
                        "keySummary" = "Spell_YasuoW_Summary"
                        "keyTooltip" = "Spell_YasuoW_Tooltip"
                        "keyCost" = "Spell_Cost_NoCost"
                        "keyTooltipExtendedBelowLine" = "Spell_YasuoW_TooltipExtendedBelowLine"
                    }
                    mLists: map[string,embed] = {
                        "LevelUp" = TooltipInstanceList {
                            LevelCount: u32 = 5
                            Elements: list[embed] = {
                                TooltipInstanceListElement {
                                    Type: string = "Effect%dAmount"
                                    TypeIndex: i32 = 5
                                    NameOverride: string = "Spell_ListType_Width"
                                }
                                TooltipInstanceListElement {
                                    Type: string = "Cooldown"
                                }
                            }
                        }
                    }
                }
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionWall {
                        CenterLocator: embed = DrawablePositionLocator {
                            DistanceOffset: f32 = 300
                            OrientationType: u32 = 3
                        }
                        Thickness: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                100
                                100
                                100
                                100
                                100
                                100
                            }
                            mValueType: u32 = 2
                        }
                        Length: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                350
                                420
                                490
                                560
                                630
                                700
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
        0x4048c61e: pointer = 0xf195e56b {
            0xec17e271: list2[embed] = {
                0xb09016f6 {
                    0x77e5e41c: u32 = 262144
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = 0xbdd28d8d
                            }
                        }
                    }
                }
                0xb09016f6 {
                    0x77e5e41c: u32 = 524288
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = 0xbdd28d8d
                            }
                        }
                    }
                }
                0xb09016f6 {
                    0x77e5e41c: u32 = 2097152
                    0x725bd4d5: pointer = GameCalculation {
                        mFormulaParts: list[pointer] = {
                            NamedDataValueCalculationPart {
                                mDataValue: hash = 0xbdd28d8d
                            }
                        }
                    }
                }
            }
            0x38382c53: list2[embed] = {
                0x150d1b92 {
                    0x0717e686: bool = false
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRKnockUpComboVFX" = SpellObject {
        mScriptName: string = "YasuoRKnockUpComboVFX"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6154
            mAlternateName: string = "Overload"
            mEffectAmount: list[embed] = {
                SpellEffectAmount {
                    Value: list[f32] = {
                        35
                        60
                        85
                        110
                        135
                        160
                        185
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        0
                        2
                        4
                        6
                        8
                        10
                        12
                    }
                }
                SpellEffectAmount {
                    Value: list[f32] = {
                        6.5
                        6.5
                        6.5
                        6.5
                        6.5
                        6.5
                        6.5
                    }
                }
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
                SpellEffectAmount {}
            }
            mCoefficient: f32 = 0.400000006
            mAnimationName: string = "Spell1"
            mCastTime: f32 = 0.25
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            mCantCancelWhileWindingUp: bool = true
            UseAnimatorFramerate: bool = true
            CastRange: list[f32] = {
                2650
                2650
                2650
                2650
                2650
                650
                650
            }
            CastConeDistance: f32 = 100
            mMissileSpec: pointer = MissileSpecification {
                MovementComponent: pointer = FixedSpeedMovement {
                    mTargetHeightAugment: f32 = 100
                    mOffsetInitialTargetHeight: f32 = 100
                    mSpeed: f32 = 2000
                }
                VerticalFacing: pointer = VeritcalFacingMatchVelocity {}
                Behaviors: list[pointer] = {
                    CastOnMovementComplete {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 1
            CastFrame: f32 = 7.5
            MissileSpeed: f32 = 2000
            mMissileEffectKey: hash = "Yasuo_R_dash"
            mHitBoneName: string = "root"
            mFloatVarsDecimals: list[i32] = {
                0
                0
                0
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
                2
            }
            SelectionPriority: u32 = 1
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        UseCasterBoundingBox: option[bool] = {
                            false
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoWMovingWallMis" = SpellObject {
        mScriptName: string = "YasuoWMovingWallMis"
        mSpell: pointer = SpellDataResource {
            mAffectsTypeFlags: u32 = 6152
            mAlternateName: string = "YasuoWMovingWall"
            mAnimationName: string = "Attack2"
            CooldownTime: list[f32] = {
                0
                0
                0
                0
                0
                0
                0
            }
            CastRange: list[f32] = {
                1200
                1200
                1200
                1200
                1200
                1200
                1200
            }
            CastRadius: list[f32] = {
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
                299.299988
            }
            CastConeDistance: f32 = 100
            LuaOnMissileUpdateDistanceInterval: f32 = 51
            mMissileSpec: pointer = MissileSpecification {
                mMissileWidth: f32 = 1
                MovementComponent: pointer = AcceleratingMovement {
                    mUseHeightOffsetAtEnd: bool = true
                    mTracksTarget: bool = false
                    mOffsetInitialTargetHeight: f32 = 100
                    mStartBoneName: string = ""
                    mProjectTargetToCastRange: bool = true
                    mAcceleration: f32 = -1200
                    mMinSpeed: f32 = 10
                    mMaxSpeed: f32 = 850
                    mInitialSpeed: f32 = 850
                }
                HeightSolver: pointer = BlendedLinearHeightSolver {}
                VerticalFacing: pointer = VerticalFacingFaceTarget {}
                Behaviors: list[pointer] = {
                    CastOnHit {}
                    DestroyOnMovementComplete {}
                }
            }
            mCastType: u32 = 3
            CastFrame: f32 = 15.0749998
            MissileSpeed: f32 = 850
            mMissileEffectName: string = "Zyra_dummy_controller.troy"
            mLineWidth: f32 = 1
            bHaveHitBone: bool = true
            mHitBoneName: string = "C_BUFFBONE_GLB_CHEST_LOC"
            SelectionPriority: u32 = 1
            mTargetingTypeData: pointer = Location {}
            mClientData: embed = SpellDataResourceClient {
                mTargeterDefinitions: list[pointer] = {
                    TargeterDefinitionRange {
                        HideWithLineIndicator: bool = true
                    }
                    TargeterDefinitionLine {
                        EndLocator: embed = DrawablePositionLocator {
                            BasePosition: u32 = 3
                        }
                        LineStopsAtEndPosition: option[bool] = {
                            false
                        }
                        LineWidth: embed = FloatPerSpellLevel {
                            mPerLevelValues: list[f32] = {
                                1
                                1
                                1
                                1
                                1
                                1
                            }
                            mValueType: u32 = 2
                        }
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Spells/YasuoRVFXClone" = SpellObject {
        mScriptName: string = "YasuoRVFXClone"
        mBuff: pointer = BuffData {
            mDescription: string = "game_buff_tooltip_RumbleDangerZone"
        }
    }
    0x16ef8788 = StatStoneSet {
        Name: string = "stat_stone_set_name_2"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "c1827f66-6df9-452a-81ef-a2ef8cb2032c"
            ItemId: u32 = 66600514
            OfferId: string = "b1a7e6ef-e46a-4dfe-9a4a-c75b2eb32e8d"
        }
        StatStones: list[link] = {
            0xbeb3b982
            0xff5b0349
            0x39ccffe5
        }
    }
    0x19ef8c41 = StatStoneSet {
        Name: string = "stat_stone_set_name_1"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "5629224b-d93f-4b41-b33c-a00ae393cf5c"
            ItemId: u32 = 66600136
            OfferId: string = "4a4a4359-52c9-4a28-90e0-02155de4bee1"
        }
        StatStones: list[link] = {
            0xcb9d3416
            0x30ef8c14
            0xfad771dc
        }
    }
    0x30ef8c14 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoWBlocks"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "0437fc71-a001-48d6-8a37-46c0bbf1bb2b"
            ItemId: u32 = 289
            OfferId: string = "c75118c9-fed9-4655-8ffa-7075472c12e9"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoWBlocks"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x0899c06d
        Milestones: list[u64] = {
            65
            175
            325
            400
            500
            200
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoWBlocks"
    }
    0xcb9d3416 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoRMulti"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "ce950611-6ca4-4d87-9c07-538a357cd889"
            ItemId: u32 = 99228
            OfferId: string = "ed8aebb0-0005-4540-a0ac-5205d20b5cea"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoRMulti"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            2
            4
            8
            10
            15
            5
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoRMulti"
    }
    0xfad771dc = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoLongRangeQ3"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "d2499ffb-3380-41fe-a400-adc2658295b9"
            ItemId: u32 = 290
            OfferId: string = "8203abfb-2ccd-4c6e-9520-4d6219f714a0"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoLongRangeQ3"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            9
            20
            45
            55
            65
            25
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoLongRangeQ3"
    }
    0x39ccffe5 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoEHits"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "6d4be337-06c8-4288-abb9-e5875687bb5b"
            ItemId: u32 = 126328
            OfferId: string = "7a9c52ef-e2e5-4da3-9c23-b285c8a7005e"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoEHits"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            9
            20
            45
            55
            65
            25
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoEHits"
    }
    0xbeb3b982 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoPBlocks"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "222cb277-f3d4-4b69-ab46-e5683e0c17cf"
            ItemId: u32 = 126327
            OfferId: string = "fa782086-c4f5-4144-aa40-c848e299e8ac"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoPBlocks"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x0899c06d
        Milestones: list[u64] = {
            5000
            13000
            25000
            30000
            38000
            15000
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoPBlocks"
    }
    0xff5b0349 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_YasuoEQCombos"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "4e5a814e-cbf2-49d1-bf4c-32d9c7229e3f"
            ItemId: u32 = 126326
            OfferId: string = "29de973b-be02-4698-ad18-f63ba6dbb868"
        }
        mDescriptionTraKey: string = "stat_stone_description_YasuoEQCombos"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 225
            }
        }
        Category: link = 0x1dab670a
        Milestones: list[u64] = {
            5
            10
            25
            30
            35
            15
        }
        EpicStatStone: bool = true
        TriggeredFromScript: bool = true
        StoneName: string = "YasuoEQCombos"
    }
    0x689564e5 = StatStoneSet {
        Name: string = "stat_stone_set_name_starter"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "12aaee6e-6909-4e79-835c-26f91bf908de"
            ItemId: u32 = 66600221
            OfferId: string = "3792477c-3d75-4864-8d60-daaf2dd15cce"
        }
        StatStones: list[link] = {
            0xa5a1bc46
            0xefb3f5d7
            0x9d0519be
        }
    }
    0x9d0519be = StatStoneData {
        mNameTraKey: string = "stat_stone_name_structures_destroyed"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "68a51516-fcd7-43b7-97f4-7cd2e6746ab5"
            ItemId: u32 = 125602
            OfferId: string = "8c694203-dd3e-4359-9d52-1b555d7e7f31"
        }
        mDescriptionTraKey: string = "stat_stone_description_StructuresDestroyed"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 53
            }
        }
        Category: link = 0x6ce57a50
        Milestones: list[u64] = {
            5
            15
            25
            30
            40
            15
        }
        StoneName: string = "YasuoStructuresDestroyed"
    }
    0xa5a1bc46 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_EpicMonstersKilled"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "6d13180b-7e4e-448d-ad56-728334777973"
            ItemId: u32 = 125600
            OfferId: string = "f0fa5a09-97f8-465a-aa16-31a3c70e11b2"
        }
        mDescriptionTraKey: string = "stat_stone_description_EpicMonstersKilled"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 55
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            0xa47810c1: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 87
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        0x47bac313: bool = false
                    }
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            0xa47810c1: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 54
                StatFilters: list[pointer] = {
                    TargetHasUnitTagFilter {
                        UnitTags: embed = ObjectTags {
                            0xa47810c1: list2[hash] = {
                                0x592aa99b
                            }
                        }
                    }
                }
            }
        }
        Category: link = 0x6ce57a50
        Milestones: list[u64] = {
            3
            10
            20
            22
            25
            10
        }
        StoneName: string = "YasuoEpicMonstersKilled"
    }
    0xefb3f5d7 = StatStoneData {
        mNameTraKey: string = "stat_stone_name_takedowns"
        CatalogEntry: embed = CatalogEntry {
            ContentId: string = "e292bb97-6b8b-40d2-9ea8-50285df3b4ac"
            ItemId: u32 = 125601
            OfferId: string = "f169d300-e173-407b-acb9-256f1d2417b2"
        }
        mDescriptionTraKey: string = "stat_stone_description_Takedowns"
        EventsToTrack: list[embed] = {
            StatStoneEventToTrack {
                EventToTrack: u32 = 7
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 87
                StatFilters: list[pointer] = {
                    TargetTypeFilter {
                        0x1e3fcd64: bool = false
                    }
                }
            }
            StatStoneEventToTrack {
                EventToTrack: u32 = 206
            }
        }
        Category: link = 0x5c6e96a2
        Milestones: list[u64] = {
            25
            65
            125
            150
            185
            75
        }
        StoneName: string = "YasuoTakedowns"
    }
    0x430da691 = ItemRecommendationOverrideSet {
        mOverrides: list[embed] = {
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapId: u32 = 11
                        0x37b75f5c: hash = "CLASSIC"
                    }
                }
                mStartingItemSets: list[embed] = {
                    ItemRecommendationOverrideStartingItemSet {
                        mStartingItems: list[hash] = {
                            "Items/1055"
                            "Items/1054"
                            "Items/1083"
                        }
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/1055"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/1054"
                            "Items/2003"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/1083"
                            "Items/2003"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/6672"
                            "Items/6671"
                            "Items/6673"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3006"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3031"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3046"
                            "Items/3095"
                            "Items/3033"
                        }
                        MaxCompletedItems: u32 = 3
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/6333"
                            "Items/3091"
                            "Items/3026"
                            "Items/3036"
                            "Items/3033"
                            "Items/3072"
                            "Items/3153"
                        }
                    }
                }
                mRecommendedItems: list[embed] = {
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6672"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6671"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6673"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3006"
                        mGroupId: u8 = 2
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3046"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3095"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3033"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3031"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6333"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3156"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3072"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3026"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3036"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3153"
                    }
                }
            }
            ItemRecommendationOverride {
                mOverrideContexts: list[embed] = {
                    ItemRecommendationOverrideContext {
                        mMapId: u32 = 12
                        0x37b75f5c: hash = "ARAM"
                    }
                }
                mStartingItemSets: list[embed] = {
                    ItemRecommendationOverrideStartingItemSet {
                        mStartingItems: list[hash] = {
                            "Items/3184"
                            "Items/3177"
                            "Items/6670"
                        }
                    }
                }
                StartingItemBundles: list[embed] = {
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/3184"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/3177"
                        }
                    }
                    ItemRecommendationOverrideStartingItemBundle {
                        Items: list[hash] = {
                            "Items/6670"
                        }
                    }
                }
                mRecItemRanges: list[embed] = {
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/6672"
                            "Items/6671"
                            "Items/6673"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3006"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3046"
                            "Items/3095"
                            "Items/3033"
                        }
                        MaxCompletedItems: u32 = 2
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/3031"
                        }
                    }
                    0x5a3bc52d {
                        Items: list[hash] = {
                            "Items/6333"
                            "Items/3091"
                            "Items/3026"
                            "Items/3036"
                            "Items/3033"
                            "Items/3072"
                            "Items/3153"
                        }
                    }
                }
                mRecommendedItems: list[embed] = {
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6672"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6671"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6673"
                        mGroupId: u8 = 1
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3006"
                        mGroupId: u8 = 2
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3046"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3095"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3033"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3031"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/6333"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3156"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3072"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3026"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3036"
                    }
                    ItemRecommendationCondition {
                        mItem: hash = "Items/3153"
                    }
                }
            }
        }
    }
    0x81cf1b08 = 0x5933da7e {
        0x5e6e4063: list[embed] = {
            RecSpellRankUpInfo {
                MapId: u32 = 12
                Position: hash = "None"
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    1
                    2
                    0
                }
            }
            RecSpellRankUpInfo {
                MapId: u32 = 11
                Position: hash = 0x4ea76b2a
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    2
                    1
                    0
                }
            }
            RecSpellRankUpInfo {
                MapId: u32 = 11
                Position: hash = 0xc982a718
                0x72e81a01: bool = true
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    2
                    1
                    0
                }
            }
            RecSpellRankUpInfo {
                MapId: u32 = 11
                Position: hash = 0xa710dc3c
                mDefaultPriority: list[u32] = {
                    3
                    0
                    2
                    1
                }
                mEarlyLevelOverrides: list[u32] = {
                    0
                    2
                    1
                    0
                }
            }
        }
    }
    0x861be7c1 = ItemRecommendationContextList {
        mAllStartingItemIds: map[u32,embed] = {
            11 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    1083
                    1054
                    1055
                    1056
                    3865
                    1027
                    1028
                    1029
                    1101
                    2031
                    1036
                    1102
                    1001
                    1052
                    1103
                    2003
                    3070
                    1082
                    2033
                }
            }
            12 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    3145
                    3044
                    1011
                    4642
                    3147
                    1042
                    3067
                    2051
                    1043
                    3801
                    2022
                    2031
                    3802
                    1036
                    6670
                    3112
                    3803
                    2003
                    1038
                    1053
                    3006
                    3057
                    3108
                    2020
                    2021
                    1026
                    6660
                    1027
                    3133
                    3184
                    2015
                    1028
                    3134
                    1029
                    3177
                    3076
                    1001
                    1052
                    3077
                    3070
                }
            }
        }
        0xa109530e: map[u32,embed] = {
            30 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    223085
                    223006
                    223508
                    223110
                    226631
                    222065
                    226675
                    223075
                    223177
                    223004
                    223504
                    226698
                    228020
                    223100
                    223071
                    223050
                    226621
                    223094
                    4017
                    223065
                    226696
                    3430
                    222051
                    223111
                    226692
                    223011
                    223165
                    223115
                    223005
                    226657
                    223036
                    223109
                    4011
                    226609
                    223161
                    223742
                    226653
                    224629
                    223047
                    223026
                    224646
                    226701
                    223020
                    226672
                    223072
                    223116
                    226697
                    224005
                    223112
                    223091
                    226662
                    223185
                    223135
                    222504
                    226664
                    223158
                    223137
                    223087
                    4010
                    228001
                    223181
                    224401
                    223102
                    223814
                    223031
                    224628
                    223156
                    223302
                    224645
                    2049
                    223152
                    226694
                    226673
                    223073
                    223146
                    223748
                    223046
                    223190
                    226617
                    224004
                    223119
                    223142
                    4015
                    223084
                    223157
                    226665
                    223107
                    224633
                    2050
                    223009
                    223153
                    223184
                    223074
                    223053
                    223003
                    226676
                    226655
                    226699
                    223078
                    223222
                    226620
                    223172
                    4016
                    223124
                    226695
                    223095
                    226616
                    223139
                    223118
                    226333
                    223089
                    223068
                    223039
                    226610
                    222502
                    223143
                    223033
                }
            }
            11 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    3152
                    6694
                    6673
                    3073
                    7021
                    3117
                    3046
                    3190
                    4643
                    6617
                    7025
                    6692
                    7040
                    7019
                    3084
                    3869
                    7042
                    3107
                    7013
                    4633
                    3748
                    7007
                    6609
                    3161
                    3742
                    3111
                    6653
                    4629
                    3155
                    6655
                    7003
                    3157
                    6699
                    3078
                    3222
                    6620
                    3072
                    7030
                    3116
                    7022
                    7001
                    6697
                    3139
                    3118
                    3089
                    3068
                    2502
                    7018
                    3143
                    3033
                    6664
                    7041
                    7012
                    3158
                    3137
                    3087
                    8001
                    3181
                    4401
                    6333
                    3110
                    6631
                    6610
                    7008
                    2065
                    7039
                    6675
                    3083
                    3004
                    3077
                    3302
                    4645
                    3050
                    6621
                    3508
                    7029
                    3094
                    3065
                    6696
                    3119
                    3142
                    3165
                    3877
                    3115
                    6665
                    6657
                    3036
                    3871
                    3109
                    3009
                    3153
                    3865
                    7038
                    7009
                    3053
                    3003
                    6676
                    7011
                    3047
                    3026
                    7034
                    7026
                    7005
                    3070
                    4646
                    6701
                    3020
                    6672
                    7028
                    3124
                    6695
                    3095
                    3074
                    6616
                    4005
                    3091
                    6662
                    3041
                    3876
                    3135
                    2504
                    7020
                    3085
                    3870
                    3006
                    7037
                    7016
                    3102
                    3814
                    3031
                    4628
                    3002
                    7031
                    3075
                    3156
                    3504
                    6698
                    8020
                    7004
                    3179
                    3100
                    3071
                }
            }
            12 = ItemRecommendationItemList {
                mItemList: list[u32] = {
                    126697
                    3152
                    6694
                    6673
                    3073
                    7021
                    3117
                    3046
                    3190
                    6617
                    7025
                    6692
                    7040
                    7019
                    3084
                    7042
                    3107
                    7013
                    4633
                    3748
                    7007
                    6609
                    3161
                    3742
                    3111
                    6653
                    4629
                    3155
                    6655
                    7003
                    3157
                    6699
                    3078
                    3222
                    6620
                    3072
                    7030
                    3116
                    7022
                    7001
                    3139
                    3118
                    3089
                    3068
                    2502
                    7018
                    3143
                    3033
                    6664
                    7041
                    7012
                    3158
                    3137
                    3087
                    8001
                    4401
                    6333
                    3110
                    6631
                    6610
                    2065
                    7039
                    6675
                    3083
                    3004
                    3077
                    3302
                    4645
                    3050
                    6621
                    3508
                    7029
                    3094
                    3065
                    6696
                    3119
                    3142
                    3165
                    3115
                    6665
                    127008
                    6657
                    3036
                    3109
                    3009
                    3153
                    7038
                    7009
                    3053
                    3003
                    6676
                    7011
                    3047
                    7034
                    7026
                    7005
                    3070
                    4646
                    6701
                    3020
                    6672
                    7028
                    3124
                    6695
                    3095
                    3074
                    6616
                    4005
                    3091
                    6662
                    3135
                    2504
                    3085
                    3006
                    7016
                    3102
                    3814
                    3031
                    4628
                    3002
                    7031
                    3075
                    3156
                    3504
                    6698
                    8020
                    7004
                    3179
                    3100
                    3071
                }
            }
        }
        mContexts: list[embed] = {
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 12
                0x37b75f5c: hash = "ARAM"
                mPosition: hash = "None"
                mIsDefaultPosition: bool = true
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1042
                                        3006
                                        2003
                                        2003
                                        6670
                                        1042
                                        2031
                                        3184
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1042
                            3006
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            2003
                            2003
                            6670
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1042
                            2031
                            3184
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/6672"
                    "Items/3031"
                    "Items/6673"
                    "Items/3153"
                    "Items/3006"
                    "Items/3091"
                    "Items/3087"
                    "Items/3072"
                    "Items/6333"
                    0x632f3551
                    "Items/6662"
                    "Items/3111"
                    "Items/3046"
                    0xf877532d
                    "Items/3084"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3087
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnI" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3006
                                    }
                                }
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                        3072
                                    }
                                }
                                "Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        3111
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        6662
                                    }
                                }
                                "AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        3111
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                        6698
                                    }
                                }
                                "AwG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3006
                                        3153
                                    }
                                }
                                "AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3153
                                    }
                                }
                                "AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        6673
                                    }
                                }
                                "AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6673
                                        3153
                                    }
                                }
                                "AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3031
                                        3111
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3091
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6672
                                        6673
                                    }
                                }
                                "Azm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6665
                                        6673
                                    }
                                }
                                "BnS" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3006
                                        3153
                                    }
                                }
                                "Bnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3084
                                    }
                                }
                                "BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3006
                                        3153
                                    }
                                }
                                "BoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3153
                                        6672
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        6673
                                    }
                                }
                                "BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        3111
                                    }
                                }
                                "BoT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                        3111
                                    }
                                }
                                "BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3031
                                        6672
                                    }
                                }
                                "e7p" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6676
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6672
                                        6673
                                    }
                                }
                                "Au+Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "Au+AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "Au+AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        6662
                                    }
                                }
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3072
                                    }
                                }
                                "Au+AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3153
                                    }
                                }
                                "Au+AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6662
                                        6673
                                    }
                                }
                                "Au+Azm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        6672
                                    }
                                }
                                "Au+Bnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3084
                                        6672
                                    }
                                }
                                "Au+BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        3091
                                    }
                                }
                                "Au+BoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        6662
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3072
                                        3091
                                    }
                                }
                                "Au+BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "AvXAvm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6665
                                    }
                                }
                                "AvXAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6333
                                    }
                                }
                                "AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        6672
                                    }
                                }
                                "AvXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6672
                                    }
                                }
                                "AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                        3072
                                    }
                                }
                                "AvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AvmAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "AvmAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "AvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "AvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "AvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6665
                                    }
                                }
                                "AvnAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6662
                                        6672
                                    }
                                }
                                "AvnAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6662
                                    }
                                }
                                "AvnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6672
                                        6673
                                    }
                                }
                                "AvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "AwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "AwAAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6662
                                    }
                                }
                                "AwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        3091
                                    }
                                }
                                "AwABoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        3091
                                    }
                                }
                                "AwFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        6631
                                    }
                                }
                                "AwFAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                        3748
                                    }
                                }
                                "AwFBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3084
                                        3111
                                        3006
                                    }
                                }
                                "AwMAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6662
                                    }
                                }
                                "AwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6672
                                    }
                                }
                                "AwMAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        6672
                                        6662
                                    }
                                }
                                "AwMBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        3111
                                    }
                                }
                                "AwMBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                        3153
                                    }
                                }
                                "AwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3111
                                    }
                                }
                                "AwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "AwPBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                        6673
                                    }
                                }
                                "AwPBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3153
                                    }
                                }
                                "AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "AwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                        3031
                                    }
                                }
                                "AwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        6673
                                    }
                                }
                                "AwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6665
                                        6673
                                    }
                                }
                                "AwTAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwTBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                        6673
                                    }
                                }
                                "AwTBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        6673
                                    }
                                }
                                "AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3111
                                    }
                                }
                                "AwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3072
                                    }
                                }
                                "AwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6662
                                        6665
                                    }
                                }
                                "AwnBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6665
                                    }
                                }
                                "AwnBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        3091
                                    }
                                }
                                "AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                                "AwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        3153
                                    }
                                }
                                "AxRAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AxRAzm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6673
                                    }
                                }
                                "AxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        3031
                                    }
                                }
                                "AxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        6672
                                    }
                                }
                                "AxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        6672
                                    }
                                }
                                "AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6662
                                    }
                                }
                                "AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        3031
                                    }
                                }
                                "AzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "Bi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "BoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6333
                                    }
                                }
                                "BoQBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIAvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        6665
                                    }
                                }
                                "Au+AvXAvm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvXAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "Au+AvXAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6672
                                    }
                                }
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "Au+AvXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvmAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                    }
                                }
                                "Au+AvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                    }
                                }
                                "Au+AwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        3091
                                    }
                                }
                                "Au+AwABoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6333
                                    }
                                }
                                "Au+AwFAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        6631
                                    }
                                }
                                "Au+AwMAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6672
                                        6665
                                    }
                                }
                                "Au+AwMBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                    }
                                }
                                "Au+AwMBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3153
                                    }
                                }
                                "Au+AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "Au+AwPBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwPBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3031
                                    }
                                }
                                "Au+AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                        3031
                                    }
                                }
                                "Au+AwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6665
                                        6673
                                    }
                                }
                                "Au+AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3072
                                    }
                                }
                                "Au+AwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6672
                                    }
                                }
                                "Au+AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        6672
                                    }
                                }
                                "Au+AxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6662
                                    }
                                }
                                "Au+AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        3031
                                    }
                                }
                                "Au+AzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "Au+Bi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3153
                                    }
                                }
                                "Au+BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6333
                                    }
                                }
                                "Au+BoQBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AvXAvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXAvmAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        3091
                                        6673
                                    }
                                }
                                "AvXAvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6662
                                    }
                                }
                                "AvXAvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3072
                                        6665
                                    }
                                }
                                "AvXAvnAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "AvXAvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXAvtBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3072
                                        3153
                                    }
                                }
                                "AvXAwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "AvXAwAAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                    }
                                }
                                "AvXAwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "AvXAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        6665
                                    }
                                }
                                "AvXAwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "AvXAwPAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAwPBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        3153
                                    }
                                }
                                "AvXAwPBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                        3091
                                    }
                                }
                                "AvXAwPBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "AvXAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6665
                                    }
                                }
                                "AvXAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3072
                                    }
                                }
                                "AvXAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        3072
                                    }
                                }
                                "AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        3072
                                    }
                                }
                                "AvXAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                        6665
                                    }
                                }
                                "AvXAxHBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        3153
                                    }
                                }
                                "AvXAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3091
                                    }
                                }
                                "AvXAxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "AvXAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3091
                                    }
                                }
                                "AvXAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3072
                                        3153
                                    }
                                }
                                "AvXBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvXBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        3091
                                    }
                                }
                                "AvXBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "AvXBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3153
                                    }
                                }
                                "AvcAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6665
                                    }
                                }
                                "AvmAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "AvnAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6673
                                    }
                                }
                                "AvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6662
                                    }
                                }
                                "AvnBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "AvnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "AwAAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6333
                                    }
                                }
                                "AwAAwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        3031
                                    }
                                }
                                "AwAAwPBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "AwAAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6333
                                    }
                                }
                                "AwAAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        3031
                                    }
                                }
                                "AwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                        3091
                                    }
                                }
                                "AwAAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6665
                                    }
                                }
                                "AwABoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        3091
                                    }
                                }
                                "AwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        3153
                                    }
                                }
                                "AwFAwMAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3748
                                        6631
                                    }
                                }
                                "AwMAwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3153
                                        6665
                                    }
                                }
                                "AwMAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6672
                                    }
                                }
                                "AwMAwnBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        6665
                                    }
                                }
                                "AwMAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6665
                                        3031
                                    }
                                }
                                "AwPAwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3153
                                    }
                                }
                                "AwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3153
                                        3031
                                    }
                                }
                                "AwPAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        3091
                                    }
                                }
                                "AwPAwnBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3091
                                    }
                                }
                                "AwPAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "AwPAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        3031
                                    }
                                }
                                "AwPAxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "AwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                    }
                                }
                                "AwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6665
                                    }
                                }
                                "AwPBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        3065
                                    }
                                }
                                "AwPBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "AwPBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6333
                                    }
                                }
                                "AwPBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AwTAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6665
                                        6673
                                    }
                                }
                                "AwTAwnBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                    }
                                }
                                "AwTAwnBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3153
                                    }
                                }
                                "AwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        3072
                                    }
                                }
                                "AwTAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3072
                                    }
                                }
                                "AwTAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6673
                                        6672
                                    }
                                }
                                "AwTAxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        6662
                                    }
                                }
                                "AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "AwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6665
                                    }
                                }
                                "AwTAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6665
                                    }
                                }
                                "AwTBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3065
                                    }
                                }
                                "AwnAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6673
                                    }
                                }
                                "AwnAxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6672
                                        6673
                                    }
                                }
                                "AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        3091
                                    }
                                }
                                "AwnAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6662
                                    }
                                }
                                "AwnAzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                    }
                                }
                                "AwnBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        3031
                                    }
                                }
                                "AwnBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "AwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6333
                                    }
                                }
                                "AxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "AxRBoGBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6672
                                        3091
                                    }
                                }
                                "AxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "AxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6333
                                    }
                                }
                                "AxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "AxRBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6662
                                    }
                                }
                                "AxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                        3091
                                    }
                                }
                                "AxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Bi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3143
                                        3031
                                    }
                                }
                                "BoGBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6665
                                    }
                                }
                                "BoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIAu+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6662
                                    }
                                }
                                "AnIAvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6662
                                    }
                                }
                                "Au+AvXAvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                    }
                                }
                                "Au+AvXAwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                    }
                                }
                                "Au+AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        6333
                                    }
                                }
                                "Au+AvXAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAwPBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3072
                                        6673
                                    }
                                }
                                "Au+AvXAwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvXAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                    }
                                }
                                "Au+AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                    }
                                }
                                "Au+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6665
                                    }
                                }
                                "Au+AvXAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                    }
                                }
                                "Au+AvXBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        3072
                                    }
                                }
                                "Au+AvXBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        3091
                                    }
                                }
                                "Au+AvXBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AwAAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwAAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                    }
                                }
                                "Au+AwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                    }
                                }
                                "Au+AwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                    }
                                }
                                "Au+AwMAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6665
                                    }
                                }
                                "Au+AwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        3031
                                    }
                                }
                                "Au+AwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                    }
                                }
                                "Au+AwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                    }
                                }
                                "Au+AwPBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        3065
                                    }
                                }
                                "Au+AwPBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "Au+AwTAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6673
                                        6672
                                    }
                                }
                                "Au+AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3031
                                    }
                                }
                                "Au+AwTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6665
                                    }
                                }
                                "Au+AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                        3065
                                    }
                                }
                                "Au+AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                    }
                                }
                                "Au+AxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                                "Au+AxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                        3091
                                    }
                                }
                                "Au+Bi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        3143
                                    }
                                }
                                "Au+BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6665
                                    }
                                }
                                "Au+BoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6662
                                    }
                                }
                                "AvXAvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        6665
                                    }
                                }
                                "AvXAvnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                        6662
                                    }
                                }
                                "AvXAwAAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        6665
                                    }
                                }
                                "AvXAwAAwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        3153
                                    }
                                }
                                "AvXAwAAwPBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        3153
                                    }
                                }
                                "AvXAwAAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6333
                                    }
                                }
                                "AvXAwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        2504
                                    }
                                }
                                "AvXAwAAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6333
                                    }
                                }
                                "AvXAwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        6665
                                    }
                                }
                                "AvXAwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAwABi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6673
                                    }
                                }
                                "AvXAwABoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6662
                                        3153
                                    }
                                }
                                "AvXAwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3091
                                    }
                                }
                                "AvXAwPAwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3072
                                        6673
                                    }
                                }
                                "AvXAwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        6665
                                    }
                                }
                                "AvXAwPAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6333
                                    }
                                }
                                "AvXAwPAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3091
                                    }
                                }
                                "AvXAwPBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        3072
                                    }
                                }
                                "AvXAwPBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                    }
                                }
                                "AvXAwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "AvXAwTAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                        3153
                                    }
                                }
                                "AvXAwTAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        3072
                                    }
                                }
                                "AvXAwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3072
                                        6333
                                    }
                                }
                                "AvXAwTAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAwTBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6673
                                        3153
                                    }
                                }
                                "AvXAwTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        3153
                                    }
                                }
                                "AvXAwTBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "AvXAwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3072
                                    }
                                }
                                "AvXAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6333
                                    }
                                }
                                "AvXAwnAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                    }
                                }
                                "AvXAwnAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAwnBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        6665
                                    }
                                }
                                "AvXAwnBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                    }
                                }
                                "AvXAwnBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3072
                                    }
                                }
                                "AvXAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6333
                                        6665
                                    }
                                }
                                "AvXAxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6662
                                        3072
                                    }
                                }
                                "AvXAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6673
                                        6665
                                    }
                                }
                                "AvXAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                    }
                                }
                                "AvXAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6673
                                        6333
                                    }
                                }
                                "AvXAxRBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3072
                                        6333
                                    }
                                }
                                "AvXAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "AvXAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        3091
                                        6333
                                    }
                                }
                                "AvXBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        3153
                                    }
                                }
                                "AvXBoGBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                    }
                                }
                                "AvXBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6333
                                    }
                                }
                                "AvXBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "AvXBoQBoRBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Av5AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "AwAAwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3031
                                    }
                                }
                                "AwPAwTAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "AwPAwTAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3031
                                    }
                                }
                                "AwPAwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3072
                                        6672
                                    }
                                }
                                "AwPAwTBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6665
                                    }
                                }
                                "AwPAwnBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        3031
                                    }
                                }
                                "AwTAwnAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6673
                                        3302
                                    }
                                }
                                "AwTAwnAxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6673
                                        3302
                                    }
                                }
                                "AwTAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "AwTAwnAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "AwTAwnBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        6665
                                    }
                                }
                                "AwTAwnBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "AwTAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3031
                                    }
                                }
                                "AwTAxRBoGBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        6672
                                    }
                                }
                                "AwTAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "AwTAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3111
                                        3072
                                    }
                                }
                                "AwTAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3072
                                    }
                                }
                                "AwTBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                        3072
                                    }
                                }
                                "AwnAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6665
                                        6673
                                    }
                                }
                                "AwnAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6662
                                    }
                                }
                                "AwnAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        3031
                                    }
                                }
                                "AwnBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        3153
                                    }
                                }
                                "AwnBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        3031
                                    }
                                }
                                "AxRBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        3072
                                    }
                                }
                                "AxRBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3031
                                        6333
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAwAAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        6333
                                    }
                                }
                                "Au+AvXAwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                    }
                                }
                                "Au+AvXAwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwABi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        6673
                                    }
                                }
                                "Au+AvXAwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXAwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAwPBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3153
                                        6665
                                    }
                                }
                                "Au+AvXAwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3072
                                    }
                                }
                                "Au+AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        3091
                                        6333
                                    }
                                }
                                "Au+AvXBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        6665
                                        3153
                                    }
                                }
                                "Au+AvXBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6333
                                    }
                                }
                                "Au+AvXBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AwPAwTBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AwTBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3031
                                    }
                                }
                                "AvXAwTAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6673
                                    }
                                }
                                "AvXAwTAwnAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AvXAwTAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3072
                                    }
                                }
                                "AvXAwTBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3153
                                        3111
                                    }
                                }
                                "AvXAwTBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        3111
                                        3153
                                    }
                                }
                                "AwTAwnBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 11
                0x37b75f5c: hash = "CLASSIC"
                mPosition: hash = 0x4ea76b2a
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1055
                                        2003
                                        1054
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                }
                0xe1100a05: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                            3869
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3006"
                    "Items/6672"
                    "Items/3031"
                    "Items/3153"
                    "Items/6673"
                    "Items/3091"
                    "Items/3072"
                    "Items/6333"
                    "Items/3087"
                    "Items/6662"
                    0x632f3551
                    "Items/3026"
                    "Items/3046"
                    "Items/3033"
                    "Items/3111"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                    }
                                }
                                "AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3091
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        6672
                                    }
                                }
                                "A8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3072
                                    }
                                }
                                "Au+Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "Au+AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3031
                                    }
                                }
                                "Au+AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3031
                                    }
                                }
                                "Au+A8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "Au+BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6673
                                        3153
                                    }
                                }
                                "AvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "AwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                    }
                                }
                                "BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAvm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        3091
                                    }
                                }
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6333
                                    }
                                }
                                "Au+AvZAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "Au+AvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6662
                                    }
                                }
                                "Au+AwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        3091
                                    }
                                }
                                "Au+AwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        6673
                                    }
                                }
                                "Au+AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        6672
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "Au+AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+Bi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+BoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvXAvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3091
                                    }
                                }
                                "AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                    }
                                }
                                "AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                    }
                                }
                                "AvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvXAvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6662
                                    }
                                }
                                "Au+AvXAwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AvXAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                    }
                                }
                                "Au+AvXAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                        3091
                                    }
                                }
                                "Au+AvXAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6665
                                        3072
                                    }
                                }
                                "Au+AvXAxHBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3091
                                    }
                                }
                                "Au+AvXAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                        6662
                                    }
                                }
                                "Au+AvXAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6665
                                    }
                                }
                                "Au+AvXBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6333
                                        3153
                                    }
                                }
                                "Au+AvXBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXBoQBt3" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvZAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvcAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                    }
                                }
                                "Au+AwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                        3091
                                    }
                                }
                                "Au+AwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "Au+AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6665
                                    }
                                }
                                "Au+AxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                                "Au+AxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3046
                                        3091
                                    }
                                }
                                "Au+AxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+AxRBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+Bi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        3091
                                    }
                                }
                                "Au+BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+BoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+BoQBoRBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvXAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvSAvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3091
                                        6333
                                    }
                                }
                                "Au+AvXAwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                    }
                                }
                                "Au+AvXAwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                    }
                                }
                                "Au+AvXAwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwABi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3026
                                        6662
                                    }
                                }
                                "Au+AvXAwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvXAwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvXAwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                        6333
                                    }
                                }
                                "Au+AvXAwTBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3026
                                        6333
                                    }
                                }
                                "Au+AvXAxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        3026
                                        3091
                                    }
                                }
                                "Au+AvXAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        3026
                                    }
                                }
                                "Au+AvXAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6333
                                    }
                                }
                                "Au+AvXAxTBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                        3091
                                    }
                                }
                                "Au+AvXBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3026
                                    }
                                }
                                "Au+AvXBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AwTAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AwTAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AwTBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AxRBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 11
                0x37b75f5c: hash = "CLASSIC"
                mPosition: hash = 0xf0ef0c24
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1101
                                        2003
                                        1102
                                        2003
                                        1055
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1101
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1102
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                }
                0xe1100a05: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                            3869
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3006"
                    "Items/6672"
                    "Items/3153"
                    "Items/3031"
                    "Items/6673"
                    "Items/3087"
                    "Items/6662"
                    "Items/3072"
                    "Items/3046"
                    "Items/3091"
                    "Items/6333"
                    "Items/3033"
                    "Items/3026"
                    "Items/3077"
                    0x632f3551
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3087
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        6673
                                    }
                                }
                                "Au+AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 11
                0x37b75f5c: hash = "CLASSIC"
                mPosition: hash = 0xc982a718
                mIsDefaultPosition: bool = true
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1055
                                        2003
                                        1054
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                }
                0xe1100a05: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                            3869
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3006"
                    "Items/6672"
                    "Items/3031"
                    "Items/3153"
                    "Items/6673"
                    "Items/3091"
                    "Items/6333"
                    "Items/3087"
                    "Items/6662"
                    "Items/3072"
                    "Items/3026"
                    "Items/3046"
                    0x632f3551
                    "Items/3111"
                    "Items/3033"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AvB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        6673
                                    }
                                }
                                "Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                        3006
                                    }
                                }
                                "AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        6672
                                    }
                                }
                                "AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3091
                                        3153
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        6672
                                    }
                                }
                                "AxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3156
                                        6672
                                    }
                                }
                                "BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                        3031
                                    }
                                }
                                "BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        6673
                                    }
                                }
                                "Au+AvZ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                    }
                                }
                                "Au+Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "Au+AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        6673
                                    }
                                }
                                "Au+AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6672
                                    }
                                }
                                "Au+AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3046
                                        3153
                                        6672
                                    }
                                }
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+Awr" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3100
                                    }
                                }
                                "Au+AxD" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3156
                                    }
                                }
                                "Au+Azm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+Bnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3084
                                    }
                                }
                                "Au+BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "Au+BoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3036
                                    }
                                }
                                "Au+Bor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3095
                                    }
                                }
                                "AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6673
                                        3153
                                    }
                                }
                                "AvmAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AvnAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "AvnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6662
                                        6673
                                    }
                                }
                                "AvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "AwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        3091
                                    }
                                }
                                "AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        6673
                                    }
                                }
                                "AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3111
                                        3006
                                        3031
                                    }
                                }
                                "AwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3091
                                        6673
                                    }
                                }
                                "AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        3091
                                    }
                                }
                                "AwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        6673
                                    }
                                }
                                "AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AxTAxU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        6662
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIAu+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvXAvm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3091
                                        6672
                                    }
                                }
                                "Au+AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3072
                                        6673
                                    }
                                }
                                "Au+AvXAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6672
                                    }
                                }
                                "Au+AvXAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6333
                                    }
                                }
                                "Au+AvXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6672
                                        6333
                                    }
                                }
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3153
                                        3091
                                    }
                                }
                                "Au+AvZAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AvZAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6662
                                    }
                                }
                                "Au+AvZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AvcAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        6673
                                    }
                                }
                                "Au+AvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AvmAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmAwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AvmAwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3077
                                    }
                                }
                                "Au+AvmAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "Au+AvmAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "Au+AvmAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "Au+AvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3153
                                    }
                                }
                                "Au+AvtBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "Au+AwAAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6333
                                    }
                                }
                                "Au+AwABoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AwFAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwFBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3084
                                        6673
                                        3153
                                    }
                                }
                                "Au+AwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6333
                                    }
                                }
                                "Au+AwPAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwPBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        3091
                                    }
                                }
                                "Au+AwTAwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "Au+AwXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AwXAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3153
                                    }
                                }
                                "Au+AwXBor" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6676
                                    }
                                }
                                "Au+AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AxDBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AxRAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        6672
                                        3031
                                    }
                                }
                                "Au+AxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3031
                                    }
                                }
                                "Au+AxRBoJ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3031
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "Au+AxTAxU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                    }
                                }
                                "Au+AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        3031
                                        3153
                                    }
                                }
                                "Au+AzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+Bi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "Au+BoQBoU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+BoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "AvXAvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6662
                                    }
                                }
                                "AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "AvXAwPAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3091
                                    }
                                }
                                "AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3091
                                    }
                                }
                                "AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6662
                                    }
                                }
                                "AvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "AvnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "AwPAwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "AwPAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwTAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3031
                                        6673
                                    }
                                }
                                "AwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "AwTAwnBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                                "AwnAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwnAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "AwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIAu+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvSAvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6662
                                    }
                                }
                                "Au+AvSAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvXAvZAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                    }
                                }
                                "Au+AvXAvZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAvmAwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AvXAvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        6673
                                    }
                                }
                                "Au+AvXAvmAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3091
                                        6665
                                    }
                                }
                                "Au+AvXAvtBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6333
                                        3153
                                    }
                                }
                                "Au+AvXAwAAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3153
                                        6673
                                    }
                                }
                                "Au+AvXAwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3091
                                    }
                                }
                                "Au+AvXAwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                        3074
                                    }
                                }
                                "Au+AvXAwPAwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3072
                                        6673
                                    }
                                }
                                "Au+AvXAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAwPAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        3153
                                        6673
                                    }
                                }
                                "Au+AvXAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3153
                                    }
                                }
                                "Au+AvXAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6333
                                    }
                                }
                                "Au+AvXAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6662
                                        6333
                                    }
                                }
                                "Au+AvXAwXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvXAwXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AvXAxDBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6665
                                    }
                                }
                                "Au+AvXAxHBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6333
                                    }
                                }
                                "Au+AvXAxRAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3033
                                        6673
                                        3046
                                    }
                                }
                                "Au+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        3091
                                    }
                                }
                                "Au+AvXAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                    }
                                }
                                "Au+AvXA6eBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6662
                                        3091
                                    }
                                }
                                "Au+AvXBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3091
                                    }
                                }
                                "Au+AvXBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        6662
                                    }
                                }
                                "Au+AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXBoQBt3" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvXBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvZAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvZAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3031
                                        6333
                                    }
                                }
                                "Au+AvZAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvZBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3026
                                    }
                                }
                                "Au+AvcAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AvmAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                    }
                                }
                                "Au+AvmAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AvmAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+AvmAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvmBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvmBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                    }
                                }
                                "Au+AvmBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+AwAAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwAAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6333
                                    }
                                }
                                "Au+AwFAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwFBnnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwFBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwPAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3026
                                    }
                                }
                                "Au+AwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6333
                                        3031
                                    }
                                }
                                "Au+AwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        3031
                                    }
                                }
                                "Au+AwPAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3026
                                    }
                                }
                                "Au+AwPBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                                "Au+AwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwTAxRAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwTAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                    }
                                }
                                "Au+AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6662
                                    }
                                }
                                "Au+AwTAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                    }
                                }
                                "Au+AxDAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AxDBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxHAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxHBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRAxTAxU" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3091
                                    }
                                }
                                "Au+AxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        3031
                                    }
                                }
                                "Au+AxRAzmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AxRBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "Au+AxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3033
                                        6673
                                    }
                                }
                                "Au+AxRBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        3031
                                    }
                                }
                                "Au+AxRBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3091
                                    }
                                }
                                "Au+AxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        3091
                                    }
                                }
                                "Au+Bi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "Au+BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+BoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3153
                                    }
                                }
                                "Au+BoQBoRBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvXAvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                    }
                                }
                                "AvXAvnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "AvXAwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "AvXAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3091
                                        6673
                                    }
                                }
                                "AvXAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                        6662
                                        3091
                                    }
                                }
                                "AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "AvnAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwTAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3087
                                        6673
                                    }
                                }
                                "AwTAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "AwnAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "AnIAu+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvSAvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3033
                                        6662
                                    }
                                }
                                "Au+AvSAvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        6665
                                    }
                                }
                                "Au+AvSAwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvXAvZAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAvZAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAvZBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        6333
                                    }
                                }
                                "Au+AvXAvcAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAvcBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAvmAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvXAvmAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAvmBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAvmBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvXAwAAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                    }
                                }
                                "Au+AvXAwAAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                        6333
                                    }
                                }
                                "Au+AvXAwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6673
                                    }
                                }
                                "Au+AvXAwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwABi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3091
                                    }
                                }
                                "Au+AvXAwABoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6665
                                    }
                                }
                                "Au+AvXAwABoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3026
                                    }
                                }
                                "Au+AvXAwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        3153
                                    }
                                }
                                "Au+AvXAwFAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AvXAwFBnnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwFBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AvXAwPAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                    }
                                }
                                "Au+AvXAwPAwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AvXAwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3072
                                    }
                                }
                                "Au+AvXAwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAwPBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAwTAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6673
                                    }
                                }
                                "Au+AvXAwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                        6662
                                    }
                                }
                                "Au+AvXAwTAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwTBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                        6665
                                    }
                                }
                                "Au+AvXAwTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                        6665
                                    }
                                }
                                "Au+AvXAwTBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvXAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AvXAwnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AvXAxDBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                    }
                                }
                                "Au+AvXAxHAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                    }
                                }
                                "Au+AvXAxHBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                    }
                                }
                                "Au+AvXAxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        6673
                                    }
                                }
                                "Au+AvXAxRBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                        6333
                                    }
                                }
                                "Au+AvXAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        6333
                                    }
                                }
                                "Au+AvXAxRBoJBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        6333
                                    }
                                }
                                "Au+AvXAxRBoQBt3" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAxRBoQBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3072
                                        6333
                                        3153
                                    }
                                }
                                "Au+AvXAxTBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAxTBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXBi9BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvXBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3091
                                    }
                                }
                                "Au+AvXBoGBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvXBoQBoRBt3" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvXBoQBoRBuB" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        6333
                                        3091
                                    }
                                }
                                "Au+AvZAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvmBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AwFBnnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAwTAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                    }
                                }
                                "Au+AwPAwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "Au+AwPAxRBi9BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AwTAxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AwTAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3026
                                    }
                                }
                                "Au+AwTAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                        6333
                                    }
                                }
                                "Au+AwTBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                    }
                                }
                                "Au+AwTBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                        6333
                                    }
                                }
                                "Au+AxRAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "Au+AxRBi9BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                    }
                                }
                                "Au+AxRBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                        3091
                                    }
                                }
                                "Au+AxRBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3031
                                        3091
                                    }
                                }
                                "Au+AxRBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6662
                                    }
                                }
                                "Au+Bi9BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3153
                                        3031
                                    }
                                }
                                "AvXAwTAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "AwPAwTAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 11
                0x37b75f5c: hash = "CLASSIC"
                mPosition: hash = 0xa710dc3c
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        1055
                                        2003
                                        1054
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1054
                            2003
                        }
                    }
                }
                0xe1100a05: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                            3869
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3006"
                    "Items/6672"
                    "Items/3153"
                    "Items/3031"
                    "Items/6673"
                    "Items/6662"
                    "Items/3091"
                    "Items/6333"
                    "Items/3072"
                    "Items/3087"
                    "Items/3033"
                    "Items/3026"
                    "Items/3046"
                    0x632f3551
                    "Items/3047"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AvZ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Avn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        6662
                                    }
                                }
                                "AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3047
                                        3031
                                    }
                                }
                                "AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3111
                                    }
                                }
                                "AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "Awn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                        3091
                                    }
                                }
                                "AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3047
                                        3111
                                    }
                                }
                                "AxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        3047
                                        3031
                                    }
                                }
                                "BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3072
                                    }
                                }
                                "Au+AvZ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                    }
                                }
                                "Au+Avm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "Au+AwA" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwF" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwM" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwX" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3046
                                        3153
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        6662
                                    }
                                }
                                "Au+AxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3156
                                    }
                                }
                                "Au+BoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+BoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        3153
                                    }
                                }
                                "AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6673
                                        3153
                                    }
                                }
                                "AvnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6662
                                        6333
                                    }
                                }
                                "AvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "AwTAwn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6672
                                    }
                                }
                                "AwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3091
                                        3302
                                    }
                                }
                                "AwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        3091
                                    }
                                }
                                "AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3006
                                        3047
                                    }
                                }
                                "BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAvm" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3072
                                        6673
                                    }
                                }
                                "Au+AvXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6672
                                        3072
                                    }
                                }
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3153
                                        3091
                                    }
                                }
                                "Au+AvZAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                        6673
                                    }
                                }
                                "Au+AvZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+AvcAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6672
                                    }
                                }
                                "Au+AvcBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+AvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6672
                                    }
                                }
                                "Au+AvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvmBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6662
                                    }
                                }
                                "Au+AwFAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwFBnn" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3084
                                    }
                                }
                                "Au+AwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AwPBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "Au+AwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        3091
                                    }
                                }
                                "Au+AwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+AwTBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwXAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRAxT" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3091
                                        6673
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "Au+AxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "Au+AxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                        3031
                                    }
                                }
                                "Au+AxtBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+Bi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+BoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        3153
                                    }
                                }
                                "Au+BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        3091
                                    }
                                }
                                "AvXAvnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        6673
                                        6662
                                    }
                                }
                                "AvXAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6333
                                    }
                                }
                                "AvnAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AvnAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "AvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6673
                                    }
                                }
                                "AvnBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                    }
                                }
                                "AwTAwnAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3031
                                        6673
                                    }
                                }
                                "AwTAwnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "AwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAvZAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                    }
                                }
                                "Au+AvXAvZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                        3072
                                    }
                                }
                                "Au+AvXAvmAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6662
                                    }
                                }
                                "Au+AvXAvmBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        6662
                                        3072
                                    }
                                }
                                "Au+AvXAvtBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6665
                                    }
                                }
                                "Au+AvXAwAAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAwABoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3091
                                    }
                                }
                                "Au+AvXAwFBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AvXAwPAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAwPBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAwTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3072
                                        6662
                                    }
                                }
                                "Au+AvXAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6673
                                        3091
                                    }
                                }
                                "Au+AvXAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6665
                                        6662
                                    }
                                }
                                "Au+AvXAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXA6eBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AvXBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        6662
                                    }
                                }
                                "Au+AvXBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3091
                                        3153
                                    }
                                }
                                "Au+AvXBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        6662
                                        3091
                                    }
                                }
                                "Au+AvZAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvZAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvZAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvZBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvcAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                        3031
                                    }
                                }
                                "Au+AvmAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AvmBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwFBnnBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwFBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6631
                                    }
                                }
                                "Au+AwPAwTAxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3031
                                    }
                                }
                                "Au+AwPAxRBi9" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3026
                                    }
                                }
                                "Au+AwPAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwPAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AwTAxRBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3031
                                        6672
                                    }
                                }
                                "Au+AwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6662
                                    }
                                }
                                "Au+AwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        6662
                                    }
                                }
                                "Au+AxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6673
                                    }
                                }
                                "Au+AxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6333
                                        3091
                                    }
                                }
                                "Au+AxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6662
                                        6333
                                    }
                                }
                                "Au+AxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+Bi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+BoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3091
                                        6333
                                    }
                                }
                                "AvXAvnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "AvXAwnAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6662
                                    }
                                }
                                "AvnAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvSAvXBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                    }
                                }
                                "Au+AvXAvZAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAwAAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6665
                                    }
                                }
                                "Au+AvXAwAAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAwABi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAwABoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                    }
                                }
                                "Au+AvXAwTAxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6673
                                    }
                                }
                                "Au+AvXAwTBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6333
                                        6662
                                    }
                                }
                                "Au+AvXAxRAxTBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3156
                                    }
                                }
                                "Au+AvXAxRBi9BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        6673
                                        3091
                                    }
                                }
                                "Au+AvXAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAxRBoJBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AvXAxRBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        3072
                                    }
                                }
                                "Au+AvXBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                        3091
                                        6662
                                    }
                                }
                                "Au+AvXBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6333
                                        3026
                                        3091
                                    }
                                }
                                "Au+AvXBoJBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AwTAxRBoGBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                    }
                                }
                                "Au+AwTAxRBoGBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AwTBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3026
                                    }
                                }
                                "Au+AxRAxTAxUBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+AxRBi9BoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                    }
                                }
                                "Au+AxRBoGBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3091
                                        3026
                                        3031
                                    }
                                }
                            }
                        }
                    }
                }
            }
            ItemRecommendationContext {
                mChampionId: u32 = 157
                mMapId: u32 = 11
                0x37b75f5c: hash = "CLASSIC"
                mPosition: hash = 0xbfc6b95f
                mStartingItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        2003
                                        2003
                                        3865
                                        1055
                                        2003
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                        ItemRecommendationMatrixRow {}
                    }
                }
                mStartingItemBundles: list[embed] = {
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            2003
                            2003
                            3865
                        }
                    }
                    ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            1055
                            2003
                        }
                    }
                }
                0xe1100a05: map[u32,embed] = {
                    3867 = ItemRecommendationItemList {
                        mItemList: list[u32] = {
                            3877
                            3869
                        }
                    }
                }
                mPopularItems: list[hash] = {
                    "Items/3006"
                    0xf49f776e
                    "Items/6672"
                    "Items/3153"
                    "Items/3031"
                    "Items/6673"
                    "Items/3087"
                    0xf29d35b1
                    "Items/3072"
                    "Items/3046"
                    0xf09f7122
                    "Items/3091"
                    "Items/6662"
                    0x632f3551
                    "Items/3111"
                }
                mCompletedItemMatrix: embed = ItemRecommendationMatrix {
                    Mrows: list[embed] = {
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "EMPTY" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3865
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3087
                                    }
                                }
                                "A8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                        6672
                                        3153
                                    }
                                }
                                "BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AwP" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AxR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                    }
                                }
                                "Au+A8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                        3877
                                    }
                                }
                                "Au+BoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                                "AxRA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                                "A8ZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3006
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AwPA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                    }
                                }
                                "Au+AxRA8Z" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        6673
                                        3031
                                    }
                                }
                                "Au+AxRBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                                "Au+A8ZA8d" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                    }
                                }
                                "Au+A8ZA8l" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                        3153
                                    }
                                }
                                "Au+A8ZBoG" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+A8ZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                        6673
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXA8ZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                        3153
                                    }
                                }
                                "Au+AxRA8ZA8d" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "Au+AxRA8ZA8l" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6672
                                    }
                                }
                                "Au+AxRA8ZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        6673
                                        6662
                                    }
                                }
                                "Au+A8ZA8dBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                    }
                                }
                                "Au+A8ZA8lBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3153
                                        3031
                                        6673
                                    }
                                }
                                "Au+A8ZBoQBoR" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                        3153
                                    }
                                }
                            }
                        }
                        ItemRecommendationMatrixRow {
                            mChoicesMap: map[string,embed] = {
                                "Au+AvXAxRA8ZBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        6673
                                    }
                                }
                                "Au+AxRA8ZA8lBoQ" = ItemRecommendationChoices {
                                    mChoices: list[u32] = {
                                        3031
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    0xeddee1ec = 0x56cec8e1 {}
    "Characters/Yasuo/CharacterRecords/Root" = CharacterRecord {
        mCharacterName: string = "Yasuo"
        BaseHp: f32 = 590
        HpPerLevel: f32 = 110
        BaseStaticHpRegen: f32 = 1.29999995
        HpRegenPerLevel: f32 = 0.180000007
        HealthBarHeight: f32 = 103
        PrimaryAbilityResource: embed = AbilityResourceSlotInfo {
            ArType: u8 = 11
            ArBaseStaticRegen: f32 = 0
            ArIncrements: f32 = 100
            ArMaxSegments: i32 = 10
            ArAllowMaxValueToBeOverridden: bool = true
        }
        BaseDamage: f32 = 60
        DamagePerLevel: f32 = 3
        BaseArmor: f32 = 30
        ArmorPerLevel: f32 = 4.5999999
        BaseSpellBlock: f32 = 32
        SpellBlockPerLevel: f32 = 2.04999995
        BaseMoveSpeed: f32 = 345
        AttackRange: f32 = 175
        AttackSpeed: f32 = 0.697000027
        AttackSpeedRatio: f32 = 0.670000017
        AttackSpeedPerLevel: f32 = 3.5
        AcquisitionRange: f32 = 400
        BasicAttack: embed = AttackSlotData {
            mAttackDelayCastOffsetPercent: option[f32] = {
                -0.0799999982
            }
            mAttackDelayCastOffsetPercentAttackSpeedRatio: option[f32] = {
                1
            }
            mAttackProbability: option[f32] = {
                1
            }
        }
        ExtraAttacks: list[embed] = {
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoBasicAttack2"
                }
            }
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoBasicAttack3"
                }
            }
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoBasicAttack4"
                }
            }
        }
        CritAttacks: list[embed] = {
            AttackSlotData {
                mAttackDelayCastOffsetPercentAttackSpeedRatio: option[f32] = {
                    1
                }
                mAttackName: option[string] = {
                    "YasuoCritAttack"
                }
            }
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoCritAttack2"
                }
            }
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoCritAttack3"
                }
            }
            AttackSlotData {
                mAttackName: option[string] = {
                    "YasuoCritAttack4"
                }
            }
        }
        SpellNames: list[string] = {
            "YasuoQ1WrapperAbility/YasuoQ1Wrapper"
            "YasuoWAbility/YasuoW"
            "YasuoEAbility/YasuoE"
            "YasuoRAbility/YasuoR"
        }
        ExtraSpells: list[string] = {
            "YasuoDummySpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
            "BaseSpell"
        }
        mAbilities: list[link] = {
            "Characters/Yasuo/Spells/YasuoRAbility"
            "Characters/Yasuo/Spells/YasuoQ1WrapperAbility"
            "Characters/Yasuo/Spells/YasuoWAbility"
            "Characters/Yasuo/Spells/YasuoEAbility"
            "Characters/Yasuo/Spells/YasuoPassiveAbility"
        }
        PassiveName: string = "game_character_passiveName_Yasuo"
        PassiveLuaName: string = "YasuoPassive"
        PassiveToolTip: string = "game_character_passiveDescription_Yasuo"
        Passive1IconName: string = "ASSETS/Characters/Yasuo/HUD/Icons2D/Yasuo_Passive.dds"
        Name: string = "game_character_displayname_Yasuo"
        WeaponMaterials: list[string] = {
            "YasuoBasicAttack"
            "YasuoBasicAttack"
            "YasuoBasicAttack"
        }
        SelectionHeight: f32 = 180
        SelectionRadius: f32 = 120
        PathfindingCollisionRadius: f32 = 32
        UnitTagsString: string = "Champion"
        mEducationToolData: embed = ToolEducationData {
            FirstItem: i32 = 1055
        }
        CharacterToolData: embed = CharacterToolData {
            MapAiPresence: map[u32,embed] = {
                0 = ToolAiPresence {
                    Medium: bool = true
                    Hard: bool = true
                }
                1 = ToolAiPresence {}
                2 = ToolAiPresence {}
            }
            PassiveData: list[embed] = {
                ToolPassiveData {
                    Name: string = "game_character_passiveName_Yasuo"
                }
            }
            SearchTags: string = "fighter"
            SearchTagsSecondary: string = "assassin"
            ChampionId: i32 = 157
            Roles: string = "ATTACKER,NIGHTMARE"
            ParFadeColor: string = "0 0 0"
            MagicRank: i32 = 4
            LevelSpellEffectiveness: f32 = 2
            DifficultyRank: i32 = 10
            Description: string = "game_character_description_Yasuo"
            DefenseRank: i32 = 4
            Classification: string = "Strong"
            ChasingAttackRangePercent: f32 = 0.5
            AttackRank: i32 = 8
        }
        PlatformEnabled: bool = true
        Flags: u32 = 8398092
        PurchaseIdentities: list[hash] = {
            "Melee"
        }
        mPreferredPerkStyle: link = "Perks/Styles/Precision"
        mPerkReplacements: embed = PerkReplacementList {
            mReplacements: list[pointer] = {
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Sorcery/ManaflowBand"
                    mReplaceWith: hash = "Perks/Styles/Sorcery/NullifyingOrb"
                }
                PerkReplacement {
                    mReplaceTarget: hash = "Perks/Styles/Precision/PresenceOfMind"
                    mReplaceWith: hash = "Perks/Styles/Precision/Triumph"
                }
            }
        }
        mCharacterPassiveSpell: link = "Characters/Yasuo/Spells/YasuoPassiveAbility/YasuoPassive"
        mCharacterPassiveBuffs: list[embed] = {
            CharacterPassiveData {
                0xbd3c31e4: link = "Characters/Yasuo/Spells/YasuoPassiveAbility/YasuoPassive"
                mComponentBuffs: list[link] = {
                    "Characters/Yasuo/Spells/YasuoPassiveCounter"
                }
            }
            CharacterPassiveData {
                0xbd3c31e4: link = "Characters/Yasuo/Spells/YasuoAnimationManager"
                mComponentBuffs: list[link] = {
                    "Characters/Yasuo/Spells/YasuoIsInCombat"
                    "Characters/Yasuo/Spells/YasuoNotInCombat"
                }
            }
            CharacterPassiveData {
                0xbd3c31e4: link = "Characters/Yasuo/Spells/YasuoSkin54Manager"
                SkinFilter: pointer = SkinFilterData {
                    SkinIds: list[u32] = {
                        54
                        55
                    }
                }
            }
        }
    }
    "Characters/Yasuo/Skins/Meta" = SkinCharacterMetaDataProperties {}
}
