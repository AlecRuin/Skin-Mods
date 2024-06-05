#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Yasuo/Animations/Skin0" = AnimationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            0x08b0f422 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle_IN.anm"
                }
            }
            0x56f6d84b = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle1.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x96ee59ff = ParticleEventData {
                        mName: hash = 0x96ee59ff
                        mStartFrame: f32 = 3
                        mEffectKey: hash = "Yasuo_BA_trail_2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Attack2.anm"
                }
            }
            0x6b01d0e8 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Sheath_Run.anm"
                }
            }
            0x401ff3c4 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run1.anm"
                }
            }
            "Run" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    0x401ff3c4
                }
            }
            "Attack3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x95ee586c = ParticleEventData {
                        mName: hash = 0x95ee586c
                        mStartFrame: f32 = 3
                        mEffectKey: hash = "Yasuo_BA_trail_3"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Attack3.anm"
                }
            }
            "Attack4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x94ee56d9 = ParticleEventData {
                        mName: hash = 0x94ee56d9
                        mEffectKey: hash = "Yasuo_BA_trail_4"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Attack4.anm"
                }
            }
            "Attack_First" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x1113e4d8 = ParticleEventData {
                        mName: hash = 0x1113e4d8
                        mStartFrame: f32 = 3
                        mEffectKey: hash = "Yasuo_BA_trail_1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Attack1.anm"
                }
            }
            "Spell1_Dash" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell1_Dash.anm"
                }
            }
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x286aa358 = JointSnapEventData {
                        mName: hash = 0x286aa358
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x3f2ba821
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell3.anm"
                }
            }
            "Run2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run2.anm"
                }
            }
            0x7edfaad7 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2.anm"
                }
            }
            "Spell2_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_180.anm"
                }
            }
            "Spell2_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_-180.anm"
                }
            }
            "Death" = AtomicClipData {
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = ParticleEventData {
                        mName: hash = "Audio_Death"
                        mEffectKey: hash = "Yasuo_Emote_death_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x286aa358 = JointSnapEventData {
                        mName: hash = 0x286aa358
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x3f2ba821
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Death.anm"
                }
            }
            0x4f00d30c = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Haste.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Characters/Yasuo/Skins/Skin0/Particles/Yasuo_Base_R_Ghosts_01" = ParticleEventData {
                    mEffectKey: hash = "Yasuo_R_Ghosts_01"
                    mParticleEventDataPairList: list[embed] = {
                        ParticleEventDataPair {
                            mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mStartFrame: f32 = 1
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell4.anm"
                }
            }
            0x49b908d9 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run1.anm"
                }
            }
            "Spell1A" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell1A.anm"
                }
            }
            "Spell1B" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell1B.anm"
                }
            }
            "Spell1C" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell1C.anm"
                }
            }
            "Spell1_Wind" = AtomicClipData {
                mFlags: u32 = 6
                mMaskDataName: hash = "Wind"
                mTrackDataName: hash = "Wind"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell1_Wind.anm"
                }
            }
            "Channel" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Channel.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Channel_Windup.anm"
                }
            }
            "Spell2_90" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_90.anm"
                }
            }
            "Spell2_-90" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_-90.anm"
                }
            }
            "Run_Fast" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Run_Fast_In"
                    "Run_Fast_Loop"
                    "Run_Fast_Loop"
                    0xf1b6fdb7
                    0x4f00d30c
                }
            }
            "Run_Fast_In" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Fast_IN.anm"
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 166
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0xeed2417d = ParticleEventData {
                        mName: hash = 0xeed2417d
                        mStartFrame: f32 = -2
                        mEffectKey: hash = "Yasuo_Emote_joke_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x4d92f4fb = SubmeshVisibilityEventData {
                        mName: hash = 0x4d92f4fb
                        mEndFrame: f32 = 2
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x4e92f68e = SubmeshVisibilityEventData {
                        mName: hash = 0x4e92f68e
                        mStartFrame: f32 = 169
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Joke.anm"
                }
            }
            "Taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Taunt" = ParticleEventData {
                        mName: hash = "Taunt"
                        mEffectKey: hash = "Yasuo_Taunt_spit"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x27e9a7fa
                            }
                        }
                        mIsLoop: bool = false
                    }
                    "Audio_Taunt" = ParticleEventData {
                        mName: hash = "Audio_Taunt"
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Yasuo_Emote_taunt_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mStartFrame: f32 = 104
                        mEndFrame: f32 = 166
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x4d92f4fb = SubmeshVisibilityEventData {
                        mName: hash = 0x4d92f4fb
                        mEndFrame: f32 = 103
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x4e92f68e = SubmeshVisibilityEventData {
                        mName: hash = 0x4e92f68e
                        mStartFrame: f32 = 167
                        mEndFrame: f32 = 222
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0xfe09406e = JointSnapEventData {
                        mName: hash = 0xfe09406e
                        mJointNameToOverride: hash = 0x31f1d317
                        mJointNameToSnapTo: hash = 0x300c9a9c
                    }
                    0x632cebf2 = ParticleEventData {
                        mName: hash = 0x632cebf2
                        mEffectKey: hash = "Yasuo_Emote_taunt_generic"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Taunt.anm"
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x0cf0606b = ParticleEventData {
                        mName: hash = 0x0cf0606b
                        mEffectKey: hash = "Yasuo_Emote_laugh_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Laugh.anm"
                }
            }
            "Spell2_0" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_0.anm"
                }
            }
            0x822d5260 = ParametricClipData {
                mFlags: u32 = 4
                mTrackDataName: hash = 0x0a8c6a47
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = "Spell2_-180"
                        mValue: f32 = -180
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_-90"
                        mValue: f32 = -90
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_0"
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_90"
                        mValue: f32 = 90
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_180"
                        mValue: f32 = 180
                    }
                }
            }
            0x3f589716 = ParametricClipData {
                mFlags: u32 = 4
                mMaskDataName: hash = 0x0a8c6a47
                mTrackDataName: hash = "Wind"
                Updater: pointer = 0x41356ce8 {}
                mParametricPairDataList: list[embed] = {
                    ParametricPairData {
                        mClipName: hash = "Spell2_-180"
                        mValue: f32 = -180
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_-90"
                        mValue: f32 = -90
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_0"
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_90"
                        mValue: f32 = 90
                    }
                    ParametricPairData {
                        mClipName: hash = "Spell2_180"
                        mValue: f32 = 180
                    }
                }
            }
            "Run_Fast_Loop" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Fast_loop.anm"
                }
            }
            0xf1b6fdb7 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0xf724b619 = JointSnapEventData {
                        mName: hash = 0xf724b619
                        mStartFrame: f32 = 32
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x66def2e7
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run1.anm"
                }
            }
            0xaec9ef19 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf724b619 = JointSnapEventData {
                        mName: hash = 0xf724b619
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x66def2e7
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle_in_Sheathed.anm"
                }
            }
            0xfb8f4ae2 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Run_Fast_IN_Sheathed"
                    0x4f00d30c
                }
            }
            "Run_Fast_IN_Sheathed" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mEventDataMap: map[hash,pointer] = {
                    0xf724b619 = JointSnapEventData {
                        mName: hash = 0xf724b619
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x66def2e7
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Fast_IN_Sheathed.anm"
                }
            }
            0xeed63eca = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Recall_loop.anm"
                }
            }
            0x5a558fb9 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Recall" = ParticleEventData {
                        mName: hash = "Recall"
                        mEffectKey: hash = 0xc542e434
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    "Audio_Recall" = ParticleEventData {
                        mName: hash = "Audio_Recall"
                        mStartFrame: f32 = 14
                        mEffectKey: hash = 0x36a5a16b
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x286aa358 = JointSnapEventData {
                        mName: hash = 0x286aa358
                        mEndFrame: f32 = 86
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x3f2ba821
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Recall.anm"
                }
            }
            "Recall" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x5a558fb9
                    0xeed63eca
                }
            }
            0x120aa0ea = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mStartFrame: f32 = 9
                        mShowSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle2.anm"
                }
            }
            0x31084864 = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x56f6d84b
                        mProbability: f32 = 6
                    }
                    SelectorPairData {
                        mClipName: hash = 0x120aa0ea
                        mProbability: f32 = 4
                    }
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x56f6d84b
                    0x31084864
                }
            }
            "Spell2" = ParallelClipData {
                mClipNameList: list[hash] = {
                    0x7edfaad7
                    0x822d5260
                }
            }
            0x18d5b1ae = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xb5ed4791 = SubmeshVisibilityEventData {
                        mName: hash = 0xb5ed4791
                        mShowSubmeshList: list[hash] = {
                            0xcf573c61
                        }
                    }
                    0xbc45bbc5 = ParticleEventData {
                        mName: hash = 0xbc45bbc5
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Yasuo_Emote_dance_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    "flute_wind" = ParticleEventData {
                        mName: hash = "flute_wind"
                        mStartFrame: f32 = 2
                        mEffectKey: hash = "Yasuo_Dance_flute_wind"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x286aa358 = JointSnapEventData {
                        mName: hash = 0x286aa358
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x3f2ba821
                    }
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                }
                mTickDuration: f32 = 0.0333333388
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Dance_loop.anm"
                }
            }
            0x4e29720f = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xb5ed4791 = SubmeshVisibilityEventData {
                        mName: hash = 0xb5ed4791
                        mStartFrame: f32 = 64
                        mShowSubmeshList: list[hash] = {
                            0xcf573c61
                        }
                    }
                    0xddf80471 = ParticleEventData {
                        mName: hash = 0xddf80471
                        mStartFrame: f32 = 35
                        mEffectKey: hash = "Yasuo_Emote_dance_in_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                    0x286aa358 = JointSnapEventData {
                        mName: hash = 0x286aa358
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x3f2ba821
                    }
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x09632d04
                        }
                    }
                    "FaceCamera" = 0xd7a6b107 {
                        0xb9cfc1ab: f32 = 135
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Dance_In.anm"
                }
            }
            "Dance" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x4e29720f
                    0x18d5b1ae
                }
            }
            "Run_Haste" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Haste.anm"
                }
            }
            0xf337510f = AtomicClipData {
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 36
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 40
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x300c9a9c
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle_IN.anm"
                }
            }
            "Sheath_Run" = AtomicClipData {
                mMaskDataName: hash = 0x8f3b0f3d
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 35
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 40
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x300c9a9c
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Sheath_Run.anm"
                }
            }
            0x300c9a9c = ConditionBoolClipData {
                Updater: pointer = 0x6c816d62 {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "Sheath_Run"
                mFalseConditionClipName: hash = 0xf337510f
            }
            "Idle_Out" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333333388
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_idle_out.anm"
                }
            }
            0x86b7dee4 = AtomicClipData {
                mFlags: u32 = 6
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run1.anm"
                }
            }
            "Run_Haste_Out" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Haste_out.anm"
                }
            }
            "Sheath_Run_Haste" = AtomicClipData {
                mMaskDataName: hash = 0x8f3b0f3d
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    0x42da2f84 = JointSnapEventData {
                        mName: hash = 0x42da2f84
                        mStartFrame: f32 = 34
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 40
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x300c9a9c
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Sheath_Run_Haste.anm"
                }
            }
            0x4f62db84 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/yasuo_run_out.anm"
                }
            }
            "Run_Out_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/yasuo_run_out_loop.anm"
                }
            }
            0x2116d5e1 = SequencerClipData {
                mFlags: u32 = 3
                mClipNameList: list[hash] = {
                    0x4f62db84
                    "Run_Out_Loop"
                }
            }
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xcf539fae = ParticleEventData {
                        mName: hash = 0xcf539fae
                        mStartFrame: f32 = 3
                        mEffectKey: hash = "Yasuo_BA_trail_1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Attack1.anm"
                }
            }
            0xc2cfde5a = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    0xc29e922c = ParticleEventData {
                        mName: hash = 0xc29e922c
                        mStartFrame: f32 = 13
                        mEffectKey: hash = "Yasuo_Emote_taunt_interactive_riven"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xf44d7fb4 = ParticleEventData {
                        mName: hash = 0xf44d7fb4
                        mStartFrame: f32 = 1
                        mEffectKey: hash = "Yasuo_Emote_taunt2_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle2.anm"
                }
            }
            0x0138ce20 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    0xcdaa1a22 = ParticleEventData {
                        mName: hash = 0xcdaa1a22
                        mStartFrame: f32 = 10
                        mEffectKey: hash = "Yasuo_Emote_taunt_interactive_ninja"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xf44d7fb4 = ParticleEventData {
                        mName: hash = 0xf44d7fb4
                        mStartFrame: f32 = 1
                        mEffectKey: hash = "Yasuo_Emote_taunt2_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle2.anm"
                }
            }
            0x6438e53a = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x73cd5838 = JointSnapEventData {
                        mName: hash = 0x73cd5838
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x27535296
                        mJointNameToSnapTo: hash = 0x73cd5838
                    }
                    0x31f1d317 = JointSnapEventData {
                        mName: hash = 0x31f1d317
                        mStartFrame: f32 = 136
                        mJointNameToOverride: hash = 0x300c9a9c
                        mJointNameToSnapTo: hash = 0x31f1d317
                    }
                    0x7baeda82 = ParticleEventData {
                        mName: hash = 0x7baeda82
                        mStartFrame: f32 = 14
                        mEffectKey: hash = "Yasuo_Emote_taunt_interactive_yi"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0xf44d7fb4 = ParticleEventData {
                        mName: hash = 0xf44d7fb4
                        mStartFrame: f32 = 1
                        mEffectKey: hash = "Yasuo_Emote_taunt2_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle2.anm"
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            "Wind" = MaskData {
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x0a8c6a47 = MaskData {
                mId: u32 = 1
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
            0x8f3b0f3d = MaskData {
                mId: u32 = 2
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    1
                    1
                    1
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            0x0a8c6a47 = TrackData {}
            "Default" = TrackData {
                mPriority: u8 = 1
            }
            "Wind" = TrackData {
                mPriority: u8 = 2
                mBlendMode: u8 = 1
            }
        }
        mSyncGroupDataMap: map[hash,embed] = {
            "Run_In" = SyncGroupData {}
            "Run" = SyncGroupData {}
        }
        mBlendDataTable: map[u64,pointer] = {
            88046832741563725 = TimeBlendData {
                mTime: f32 = 0
            }
            626268775573227493 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268777199151831 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268777825354509 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268778106600334 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268778244128077 = TimeBlendData {
                mTime: f32 = 0
            }
            626268778335450667 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268778352228286 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268778369005905 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            886425409903181133 = TimeBlendData {
                mTime: f32 = 0
            }
            1300028369835263973 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028371461188311 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372087390989 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372368636814 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372506164557 = TimeBlendData {
                mTime: f32 = 0
            }
            1300028372597487147 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372614264766 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372631042385 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1789531791005629773 = TimeBlendData {
                mTime: f32 = 0
            }
            2158921752002299877 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921753004469725 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921753628224215 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921754254426893 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921754535672718 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921754673200461 = TimeBlendData {
                mTime: f32 = 0
            }
            2158921754764523051 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921754781300670 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2158921754798078289 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2384328218257177933 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613710324378 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614137439172 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614387057420 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614558138472 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614856884456 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597615816393485 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2432597616235167053 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235697150344525 = TimeBlendData {
                mTime: f32 = 0
            }
            2975735349376499021 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952482581837 = TimeBlendData {
                mTime: f32 = 0
            }
            3462312211520208205 = TimeBlendData {
                mTime: f32 = 0
            }
            3533153505179647309 = TimeBlendData {
                mTime: f32 = 0
            }
            3756553759474892109 = TimeBlendData {
                mTime: f32 = 0
            }
            3810001195794742605 = TimeBlendData {
                mTime: f32 = 0
            }
            4199991338737384781 = TimeBlendData {
                mTime: f32 = 0
            }
            4564564346258636109 = TimeBlendData {
                mTime: f32 = 0
            }
            4620679766347220965 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679766920393668 = TimeBlendData {
                mTime: f32 = 0
            }
            4620679767973145303 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679768599347981 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679768880593806 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679769018121549 = TimeBlendData {
                mTime: f32 = 0
            }
            4620679769109444139 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679769126221758 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679769142999377 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5312286964063799269 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5312286966315926285 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5312286966734699853 = TimeBlendData {
                mTime: f32 = 0
            }
            5312286966826022443 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5312286966842800062 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5312286966859577681 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5632158220927155533 = TimeBlendData {
                mTime: f32 = 0
            }
            5692781977992038373 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5692781980244165389 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5692781980662938957 = TimeBlendData {
                mTime: f32 = 0
            }
            5692781980754261547 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5692781980771039166 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5692781980787816785 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5720375839869680973 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852524741101541 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852526367025879 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852526993228557 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852527274474382 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852527412002125 = TimeBlendData {
                mTime: f32 = 0
            }
            6030852527503324715 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852527520102334 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6030852527536879953 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6247030502141246797 = TimeBlendData {
                mTime: f32 = 0
            }
            6266433748669433829 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433750295358167 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433750921560845 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433751202806670 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433751340334413 = TimeBlendData {
                mTime: f32 = 0
            }
            6266433751431657003 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433751448434622 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433751465212241 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149149289842661 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149150915766999 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149151541969677 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149151823215502 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149151960743245 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149152052065835 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149152068843454 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149152085621073 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569501297313765 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569502923238103 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569503549440781 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569503830686606 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569503968214349 = TimeBlendData {
                mTime: f32 = 0
            }
            6427569504059536939 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569504076314558 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6427569504093092177 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208474199590885 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208475825515223 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476451717901 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476732963726 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476961814059 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476978591678 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476995369297 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6509266864339205453 = TimeBlendData {
                mTime: f32 = 0
            }
            6521126347080252749 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302194646349 = TimeBlendData {
                mTime: f32 = 0
            }
            7221774042933017933 = TimeBlendData {
                mTime: f32 = 0
            }
            7710673732388653029 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673734014577367 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673734640780045 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673734922025870 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673735059553613 = TimeBlendData {
                mTime: f32 = 0
            }
            7710673735150876203 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673735167653822 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7710673735184431441 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7909614047524863309 = TimeBlendData {
                mTime: f32 = 0
            }
            8089728032273120589 = TimeBlendData {
                mTime: f32 = 0
            }
            8291053126953600997 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053128381349092 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053128579525335 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053129205728013 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053129486973838 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053129624501581 = TimeBlendData {
                mTime: f32 = 0
            }
            8291053129715824171 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053129732601790 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8291053129749379409 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152163233335269 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152164235505117 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152165485462285 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152165904235853 = TimeBlendData {
                mTime: f32 = 0
            }
            8871152165995558443 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152166012336062 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            8871152166029113681 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213609482749925 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213611108674263 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213611734876941 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213612016122766 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213612153650509 = TimeBlendData {
                mTime: f32 = 0
            }
            9142213612244973099 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213612261750718 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9142213612278528337 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9380244174326512973 = TimeBlendData {
                mTime: f32 = 0
            }
            9707472595827866957 = TimeBlendData {
                mTime: f32 = 0
            }
            11374364255402376525 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634412495629 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733634831269197 = TimeBlendData {
                mTime: f32 = 0
            }
            11920329799306362189 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939629678542157 = TimeBlendData {
                mTime: f32 = 0
            }
            12579309087834161933 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12579309088252935501 = TimeBlendData {
                mTime: f32 = 0
            }
            12594860726745087309 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675252671907813 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675254297832151 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675254924034829 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255205280654 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255434130987 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255450908606 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255467686225 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13111734580252556621 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006022188365 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853227401152485 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853229653279501 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230072053069 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230163375659 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230180153278 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853230196930897 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13616715450274069837 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352411149600741 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413401727757 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413911823915 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413928601534 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413945379153 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            14022579950837744397 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14022579951256517965 = TimeBlendData {
                mTime: f32 = 0
            }
            14022579951347840555 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14022579951364618174 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14022579951381395793 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14037683044839112013 = TimeBlendData {
                mTime: f32 = 0
            }
            14094639275747492621 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14094639276166266189 = TimeBlendData {
                mTime: f32 = 0
            }
            14094639276257588779 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14094639276274366398 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14094639276291144017 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14166698600657240845 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14166698601076014413 = TimeBlendData {
                mTime: f32 = 0
            }
            14166698601167337003 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14166698601184114622 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14166698601200892241 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14683847156396768589 = TimeBlendData {
                mTime: f32 = 0
            }
            14777090760578041829 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14777090761580211677 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14777090762830168845 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14777090763248942413 = TimeBlendData {
                mTime: f32 = 0
            }
            14777090763340265003 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14777090763357042622 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14777090763373820241 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            17210012066520808781 = TimeBlendData {
                mTime: f32 = 0
            }
            17417387574496378189 = TimeBlendData {
                mTime: f32 = 0
            }
            17525565602975497549 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            18126789362886163789 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
