#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Yasuo/Animations/Skin9" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
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
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Attack1.anm"
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
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Attack2.anm"
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
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Attack3.anm"
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
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Attack4.anm"
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
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Attack1.anm"
                }
            }
            "Channel" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x401b5570 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_channel_loop.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_channel_windup.anm"
                }
            }
            "Dance" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x4e29720f
                    0x18d5b1ae
                }
            }
            0x4e29720f = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xddf80471 = SoundEventData {
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_Cast"
                        mIsLoop: bool = false
                    }
                    0xae018423 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 25
                        mShowSubmeshList: list[hash] = {
                            0x2b4481f2
                        }
                    }
                    0xaf0185b6 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 149
                        mShowSubmeshList: list[hash] = {
                            0xdcd84140
                        }
                    }
                    0xb0018749 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 149
                        mShowSubmeshList: list[hash] = {
                            0xddd842d3
                        }
                    }
                    0xb10188dc = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 149
                        mShowSubmeshList: list[hash] = {
                            0xe2d84ab2
                        }
                    }
                    0x9479f5ae = ParticleEventData {
                        mStartFrame: f32 = 149
                        mEndFrame: f32 = 165
                        mEffectKey: hash = "Yasuo_Z_Dance_Burst"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0x35d439d2 = ParticleEventData {
                        mStartFrame: f32 = 150
                        mEndFrame: f32 = 187
                        mEffectKey: hash = "Yasuo_Z_Dance_Glow_FireBro_S"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                        mIsKillEvent: bool = false
                    }
                    0x73de3283 = ParticleEventData {
                        mStartFrame: f32 = 36
                        mEndFrame: f32 = 168
                        mEffectKey: hash = "Yasuo_Z_Dance_Glow_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0xe1efb070 = ParticleEventData {
                        mStartFrame: f32 = 150
                        mEndFrame: f32 = 187
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x905cfba7
                            }
                        }
                    }
                    0x04db553c = ParticleEventData {
                        mStartFrame: f32 = 150
                        mEndFrame: f32 = 187
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x8f5cfa14
                            }
                        }
                    }
                    0xef56d540 = ParticleEventData {
                        mStartFrame: f32 = 150
                        mEndFrame: f32 = 187
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x8e5cf881
                            }
                        }
                    }
                    0x7cf4f4d7 = ParticleEventData {
                        mStartFrame: f32 = 33
                        mEndFrame: f32 = 60
                        mEffectKey: hash = "Yasuo_Z_Joke_PopOut"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Gourd"
                            }
                        }
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Dance_enter.anm"
                }
            }
            0x18d5b1ae = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x499ad2f0 = SoundEventData {
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x4c9ad7a9 = SoundEventData {
                        mStartFrame: f32 = 40
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x4b9ad616 = SoundEventData {
                        mStartFrame: f32 = 82
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x4e9adacf = SoundEventData {
                        mStartFrame: f32 = 124
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x4d9ad93c = SoundEventData {
                        mStartFrame: f32 = 164
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x509addf5 = SoundEventData {
                        mStartFrame: f32 = 206
                        mSoundName: string = "Play_sfx_yasuoSkin09_Dance3d_drum"
                    }
                    0x8a9e61f1 = SoundEventData {
                        mStartFrame: f32 = 120
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_fire_oc"
                    }
                    0x899e605e = SoundEventData {
                        mStartFrame: f32 = 180
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_fire_oc"
                    }
                    0x8c9e6517 = SoundEventData {
                        mStartFrame: f32 = 240
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_fire_oc"
                    }
                    0xf9a548b9 = SoundEventData {
                        mStartFrame: f32 = 55
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_fire_oc"
                    }
                    0xd3e4341c = SoundEventData {
                        mSoundName: string = "Play_sfx_YasuoSkin09_Dance3D_fire_loop_01"
                    }
                    0xae018423 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0x2b4481f2
                        }
                    }
                    0xaf0185b6 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xdcd84140
                        }
                    }
                    0xb0018749 = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xddd842d3
                        }
                    }
                    0xb10188dc = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xe2d84ab2
                        }
                    }
                    0xe1efb070 = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x905cfba7
                            }
                        }
                    }
                    0x04db553c = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x8f5cfa14
                            }
                        }
                    }
                    0xef56d540 = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0x8e5cf881
                            }
                        }
                    }
                    0xc5a0ddcc = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Dance_Idle_FireBro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0x73de3283 = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Dance_Glow_FireBro_S"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mTickDuration: f32 = 0.0333333388
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Dance_loop.anm"
                }
            }
            "death" = AtomicClipData {
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Death" = SoundEventData {
                        mStartFrame: f32 = 29
                        mSoundName: string = "Play_sfx_YasuoSkin09_Death3D_cast"
                        mIsLoop: bool = false
                    }
                    0xc2b9d0c8 = ParticleEventData {
                        mEndFrame: f32 = 102
                        mEffectKey: hash = "Yasuo_Z_Death_BuildUp"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "R_Buffbone_Glb_Hand_Loc"
                            }
                        }
                    }
                    0xaba725f7 = ParticleEventData {
                        mStartFrame: f32 = 105
                        mEffectKey: hash = "Yasuo_Z_Death_Crack"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                        mIsLoop: bool = false
                    }
                    0x3f220578 = ParticleEventData {
                        mStartFrame: f32 = 100
                        mEffectKey: hash = "Yasuo_Z_Death_Explode"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "R_Buffbone_Glb_Hand_Loc"
                            }
                        }
                    }
                    0xde0f150d = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Death_Impact"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Chest_Loc"
                            }
                        }
                    }
                    "Hide" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 106
                        mHideSubmeshList: list[hash] = {
                            0x5fa0763e
                            "BODY"
                            0xfdc21006
                        }
                    }
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 3
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                    0x5fa3c247 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 80
                        mHideSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Death.anm"
                }
            }
            "Idle1" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0x56f6d84b
                    0x31084864
                }
            }
            0x56f6d84b = AtomicClipData {
                mFlags: u32 = 1
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Idle1.anm"
                }
            }
            0x120aa0ea = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Idle" = SoundEventData {
                        mStartFrame: f32 = 17
                        mSoundName: string = "Play_sfx_yasuo_skin09_idle_spike_oc"
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "Spikes" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Idle2.anm"
                }
            }
            0xb99d8609 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Idle" = SoundEventData {
                        mStartFrame: f32 = 40
                        mSoundName: string = "Play_sfx_yasuo_skin09_idle_spike02_oc"
                        mIsLoop: bool = false
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "Spikes" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Idle3.anm"
                }
            }
            0x08b0f422 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "Buffbone_Glb_Channel_Loc"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_idle_in.anm"
                }
            }
            "Idle_Run_Trans" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Sword2LHandSheath" = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Idle_Run_Trans.anm"
                }
            }
            0xaec9ef19 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                    0xf724b619 = JointSnapEventData {
                        mName: hash = 0xf724b619
                        mJointNameToOverride: hash = "L_Hair1"
                        mJointNameToSnapTo: hash = "Sheath"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Idle_in_Sheathed.anm"
                }
            }
            0x31084864 = SelectorClipData {
                mFlags: u32 = 2
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = 0x56f6d84b
                        mProbability: f32 = 70
                    }
                    SelectorPairData {
                        mClipName: hash = 0x120aa0ea
                        mProbability: f32 = 15
                    }
                    SelectorPairData {
                        mClipName: hash = 0xb99d8609
                        mProbability: f32 = 15
                    }
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xeed2417d = SoundEventData {
                        mSoundName: string = "Play_sfx_YasuoSkin09_Joke3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    "Flame" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 78
                        mEndFrame: f32 = 259
                        mShowSubmeshList: list[hash] = {
                            0x2b4481f2
                        }
                    }
                    0x4541e79d = ParticleEventData {
                        mStartFrame: f32 = 83
                        mEndFrame: f32 = 259
                        mEffectKey: hash = "Yasuo_Z_Joke_Firebro"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0x65437f94 = ParticleEventData {
                        mStartFrame: f32 = 254
                        mEffectKey: hash = "Yasuo_Z_Joke_Firebro_Death"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0xed010ae2 = ParticleEventData {
                        mStartFrame: f32 = 83
                        mEndFrame: f32 = 240
                        mEffectKey: hash = "Yasuo_Z_Joke_Firebro_Idle"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = 0xcb01362a
                            }
                        }
                    }
                    0xba347e70 = ParticleEventData {
                        mStartFrame: f32 = 58
                        mEffectKey: hash = "Yasuo_Z_Joke_Open"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Gourd"
                            }
                        }
                    }
                    0x1f4b4461 = ParticleEventData {
                        mStartFrame: f32 = 83
                        mEffectKey: hash = "Yasuo_Z_Joke_PopOut"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Gourd"
                            }
                        }
                    }
                    0xcd528e5e = ParticleEventData {
                        mStartFrame: f32 = 304
                        mEndFrame: f32 = 308
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Buffbone_Glb_Weapon_1"
                            }
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Joke.anm"
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x0cf0606b = SoundEventData {
                        mStartFrame: f32 = 2
                        mSoundName: string = "Play_sfx_YasuoSkin09_Laugh3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    0xcb59e201 = ParticleEventData {
                        mStartFrame: f32 = 19
                        mEndFrame: f32 = 65
                        mEffectKey: hash = "Yasuo_Z_Laugh_AvatarGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Buffbone_Glb_Channel_Loc"
                            }
                        }
                    }
                    0xcef6a86c = ParticleEventData {
                        mStartFrame: f32 = 9
                        mEndFrame: f32 = 20
                        mEffectKey: hash = "Yasuo_Z_Laugh_Trail"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "R_Buffbone_Glb_Hand_Loc"
                            }
                        }
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    0x9ce64f57 = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 3
                        mEndFrame: f32 = 78
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Laugh.anm"
                }
            }
            "Recall" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Recall" = SoundEventData {
                        mSoundName: string = "Play_sfx_yasuo_skin09_recall_leadin_01"
                        mIsLoop: bool = false
                    }
                    0x6256dcac = ParticleEventData {
                        mStartFrame: f32 = 165
                        mEndFrame: f32 = 270
                        mEffectKey: hash = "Yasuo_Z_Recall_BodyGlow"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Chest_Loc"
                            }
                        }
                    }
                    0xda6386b1 = ParticleEventData {
                        mStartFrame: f32 = 52
                        mEndFrame: f32 = 60
                        mEffectKey: hash = "Yasuo_Z_Recall_HeadSmash"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Head_Loc"
                            }
                        }
                    }
                    0x87161a42 = ParticleEventData {
                        mStartFrame: f32 = 95
                        mEndFrame: f32 = 270
                        mEffectKey: hash = "Yasuo_Z_Recall_Spikes"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Chest_Loc"
                            }
                        }
                    }
                    0xdf24174f = ParticleEventData {
                        mStartFrame: f32 = 95
                        mEndFrame: f32 = 100
                        mEffectKey: hash = "Yasuo_Z_Recall_Transform_01"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Chest_Loc"
                            }
                        }
                    }
                    0x95a926cd = ParticleEventData {
                        mStartFrame: f32 = 165
                        mEndFrame: f32 = 170
                        mEffectKey: hash = "Yasuo_Z_Recall_Transform_02"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Chest_Loc"
                            }
                        }
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "HEAD" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 169
                        mShowSubmeshList: list[hash] = {
                            0xfcc20e73
                        }
                        mHideSubmeshList: list[hash] = {
                            0xfdc21006
                        }
                    }
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 93
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Recall.anm"
                }
            }
            "Recall_Winddown" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "audio_recall_winddown" = SoundEventData {
                        mName: hash = "audio_recall_winddown"
                        mSoundName: string = "Play_sfx_YasuoSkin03_Recall_winddown"
                        mIsLoop: bool = false
                    }
                    0xcc8e8924 = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Respawn_Crater"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                    }
                    0x5fce7f73 = ParticleEventData {
                        mStartFrame: f32 = 1
                        mEndFrame: f32 = 20
                        mEffectKey: hash = "Yasuo_Z_Respawn"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                            ParticleEventDataPair {
                                mBoneName: hash = "Hair1"
                            }
                        }
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Respawn.anm"
                }
            }
            "Respawn" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "audio_respawn" = SoundEventData {
                        mSoundName: string = "play_sfx_yasuo_skin09_idle_respawn"
                        mIsLoop: bool = false
                    }
                    0xcc8e8924 = ParticleEventData {
                        mEffectKey: hash = "Yasuo_Z_Respawn_Crater"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                    }
                    0x5fce7f73 = ParticleEventData {
                        mEndFrame: f32 = 20
                        mEffectKey: hash = "Yasuo_Z_Respawn"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Hair1"
                            }
                        }
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Respawn.anm"
                }
            }
            0x6b01d0e8 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Sheath_Run1.anm"
                }
            }
            0x401ff3c4 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    0x6fd8bac2 = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1.anm"
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
            0x4f00d30c = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run_Haste.anm"
                }
            }
            0xfb8f4ae2 = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Run_Fast_IN_Sheathed"
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
            "Run_Fast_IN_Sheathed" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mEventDataMap: map[hash,pointer] = {
                    0xf724b619 = JointSnapEventData {
                        mName: hash = 0xf724b619
                        mJointNameToOverride: hash = "L_Hair1"
                        mJointNameToSnapTo: hash = "Sheath"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Run_Fast_IN_Sheathed.anm"
                }
            }
            0xf1b6fdb7 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1.anm"
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
            "Run_Haste" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "Sheath2LHand" = JointSnapEventData {
                        mName: hash = "Sheath2LHand"
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                    0x4100ffc8 = SubmeshVisibilityEventData {
                        mName: hash = 0x4100ffc8
                        mHideSubmeshList: list[hash] = {
                            0x2d891448
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run_Homeguard.anm"
                }
            }
            "Run_Homeguard" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run_Homeguard.anm"
                }
            }
            0x49b908d9 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run_In"
                mEventDataMap: map[hash,pointer] = {
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "Sheath2LHand" = JointSnapEventData {
                        mName: hash = "Sheath2LHand"
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1.anm"
                }
            }
            "Run_Idle_Trans" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Sheath2LHand" = JointSnapEventData {
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run_Idle_Trans.anm"
                }
            }
            "Sheath" = ConditionBoolClipData {
                Updater: pointer = IsMovingParametricUpdater {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = "Sheath_Run"
                mFalseConditionClipName: hash = 0xf337510f
            }
            0xf337510f = AtomicClipData {
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    0x61aca863 = SoundEventData {
                        mStartFrame: f32 = 20
                        mSoundName: string = "Play_sfx_YasuoSkin09_YasuoSheathSpark_buffactivate"
                        mIsLoop: bool = false
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 25
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Sheath"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mStartFrame: f32 = 26
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_idle_in.anm"
                }
            }
            "Sheath_Run" = AtomicClipData {
                mMaskDataName: hash = 0x8f3b0f3d
                mTrackDataName: hash = 0x0a8c6a47
                mEventDataMap: map[hash,pointer] = {
                    0x61aca863 = SoundEventData {
                        mStartFrame: f32 = 26
                        mSoundName: string = "Play_sfx_YasuoSkin09_YasuoSheathSpark_buffactivate"
                        mIsLoop: bool = false
                    }
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mStartFrame: f32 = 28
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 27
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Sheath"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Sheath_Run1.anm"
                }
            }
            "Spell1A" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 9
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                    "submesh" = SubmeshVisibilityEventData {
                        mEndFrame: f32 = 8
                        mHideSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell1A.anm"
                }
            }
            "Spell1B" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 9
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell1B.anm"
                }
            }
            "Spell1C" = ConditionBoolClipData {
                mFlags: u32 = 4
                Updater: pointer = IsMovingParametricUpdater {}
                mChangeAnimationMidPlay: bool = true
                mTrueConditionClipName: hash = 0x37179eeb
                mFalseConditionClipName: hash = 0xb329a867
            }
            0xb329a867 = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 9
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell1C.anm"
                }
            }
            0x37179eeb = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 9
                        mEndFrame: f32 = 44
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell1Crun.anm"
                }
            }
            "Spell1_Dash" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf4ea4345 = SubmeshVisibilityEventData {
                        mName: hash = 0xf4ea4345
                        mShowSubmeshList: list[hash] = {
                            0x2d891448
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_skin09_Spell1_Dash.anm"
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
            "Spell2" = ParallelClipData {
                mClipNameList: list[hash] = {
                    "Spell2_BASE"
                    0x822d5260
                }
            }
            "Spell2_-180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Spell2_-180.anm"
                }
            }
            "Spell2_-90" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell2_-90.anm"
                }
            }
            "Spell2_0" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xe61cac07 = ParticleEventData {
                        mName: hash = 0xcf539fae
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
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_skin09_Spell2_0.anm"
                }
            }
            "Spell2_180" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell2_180.anm"
                }
            }
            "Spell2_90" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell2_90.anm"
                }
            }
            "Spell2_BASE" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_skin09_Spell2.anm"
                }
            }
            0x822d5260 = ParametricClipData {
                mFlags: u32 = 4
                mTrackDataName: hash = 0x0a8c6a47
                Updater: pointer = LookAtSpellTargetAngleParametricUpdater {}
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
                Updater: pointer = LookAtSpellTargetAngleParametricUpdater {}
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
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Spikes" = SubmeshVisibilityEventData {
                        mStartFrame: f32 = 1
                        mShowSubmeshList: list[hash] = {
                            "Spikes"
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell3.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x161b58e4 = ParticleEventData {
                        mStartFrame: f32 = 13
                        mEffectKey: hash = "Yasuo_R_Charge_01"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "SwordBlade2"
                            }
                        }
                    }
                    0x03d4b82e = ParticleEventData {
                        mStartFrame: f32 = 25
                        mEffectKey: hash = "Yasuo_R_Swipe_01"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "BUFFBONE_GLB_GROUND_LOC"
                            }
                        }
                    }
                    0x78c7c40f = ParticleEventData {
                        mStartFrame: f32 = 10
                        mEffectKey: hash = "Yasuo_R_Charge_01"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "SwordBlade2"
                            }
                        }
                    }
                    "Sword" = SubmeshVisibilityEventData {
                        mShowSubmeshList: list[hash] = {
                            0xc2cdac4f
                        }
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell4.anm"
                }
            }
            "Spell4_Trans" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Spell4_trans.anm"
                }
            }
            "taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x61aca863 = SoundEventData {
                        mStartFrame: f32 = 190
                        mSoundName: string = "Play_sfx_YasuoSkin09_YasuoSheathSpark_buffactivate"
                        mIsLoop: bool = false
                    }
                    "Audio_Taunt" = SoundEventData {
                        mSoundName: string = "Play_sfx_YasuoSkin09_Taunt3D_buffactivate"
                        mIsLoop: bool = false
                    }
                    0xb9208287 = ParticleEventData {
                        mStartFrame: f32 = 77
                        mEndFrame: f32 = 90
                        mEffectKey: hash = "Yasuo_Z_Tuant_FireBreath_01"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Head_Loc"
                            }
                        }
                    }
                    0x48825dd5 = ParticleEventData {
                        mStartFrame: f32 = 152
                        mEndFrame: f32 = 162
                        mEffectKey: hash = "Yasuo_Z_Tuant_FireBreath_02"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_Glb_Head_Loc"
                            }
                        }
                        mIsDetachable: bool = true
                    }
                    0x4b08fc94 = ParticleEventData {
                        mStartFrame: f32 = 82
                        mEndFrame: f32 = 192
                        mEffectKey: hash = "Yasuo_Z_Taunt_Sword_Fire"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "SwordBlade2"
                            }
                        }
                    }
                    0x8ddfcf58 = ParticleEventData {
                        mStartFrame: f32 = 124
                        mEndFrame: f32 = 140
                        mEffectKey: hash = "Yasuo_Z_Taunt_Sword_Flick"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Cstm_Buffbone_Weapon_Tip"
                            }
                        }
                    }
                    0xcd528e5e = ParticleEventData {
                        mStartFrame: f32 = 195
                        mEndFrame: f32 = 200
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Buffbone_Glb_Weapon_1"
                            }
                        }
                    }
                    0x6fd8bac2 = JointSnapEventData {
                        mStartFrame: f32 = 195
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                }
                mTickDuration: f32 = 0.0333329998
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Taunt.anm"
                }
            }
            "Idle_Out" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                }
                mTickDuration: f32 = 0.0333333388
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_idle_out.anm"
                }
            }
            "Run" = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    0x401ff3c4
                }
            }
            "Run_Haste_Out" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    "Sheath2LHand" = JointSnapEventData {
                        mName: hash = "Sheath2LHand"
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run_Haste_Out.anm"
                }
            }
            0x86b7dee4 = AtomicClipData {
                mFlags: u32 = 6
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    "Sword2LHandSheath" = JointSnapEventData {
                        mName: hash = "Sword2LHandSheath"
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword_Sheathed"
                    }
                    "Sheath2LHand" = JointSnapEventData {
                        mName: hash = "Sheath2LHand"
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1.anm"
                }
            }
            0x2116d5e1 = SequencerClipData {
                mFlags: u32 = 3
                mClipNameList: list[hash] = {
                    0x4f62db84
                    "Run_Out_Loop"
                }
            }
            "Run_Out_Loop" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1_Out_Loop.anm"
                }
            }
            0x4f62db84 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mSyncGroupDataName: hash = "Run"
                mEventDataMap: map[hash,pointer] = {
                    "SnapBuffbone" = JointSnapEventData {
                        mJointNameToOverride: hash = "C_Buffbone_Glb_Center_Loc"
                        mJointNameToSnapTo: hash = "root"
                    }
                    0x879eb7f7 = JointSnapEventData {
                        mJointNameToOverride: hash = "BUFFBONE_GLB_GROUND_LOC"
                        mJointNameToSnapTo: hash = "C_Buffbone_GLB_Layout_Loc"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Skin09/Animations/Yasuo_Skin09_Run1_Out.anm"
                }
            }
            "Sheath_Run_Haste" = AtomicClipData {
                mMaskDataName: hash = 0x8f3b0f3d
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0x61aca863 = SoundEventData {
                        mStartFrame: f32 = 34
                        mSoundName: string = "Play_sfx_YasuoSkin09_YasuoSheathSpark_buffactivate"
                        mIsLoop: bool = false
                    }
                    "Sheath2LHand" = JointSnapEventData {
                        mName: hash = "Sheath2LHand"
                        mJointNameToOverride: hash = "Sheath"
                        mJointNameToSnapTo: hash = "Sheath2LHand"
                    }
                    "sheath_spark" = ParticleEventData {
                        mName: hash = "sheath_spark"
                        mStartFrame: f32 = 40
                        mEffectKey: hash = "Yasuo_I_sheath_spark"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "Sheath"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x42da2f84 = JointSnapEventData {
                        mName: hash = 0x42da2f84
                        mStartFrame: f32 = 34
                        mJointNameToOverride: hash = "Sword"
                        mJointNameToSnapTo: hash = "Sword2LHandSheath"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Yasuo/Skins/Base/Animations/Yasuo_Sheath_Run_Haste.anm"
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
                    1
                    0
                    1
                    1
                    0
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
                    1
                    1
                    1
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
                }
            }
            0x8f3b0f3d = MaskData {
                mId: u32 = 2
                mWeightList: list[f32] = {
                    0
                    0
                    0
                    1
                    1
                    0
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
                    0
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
                    1
                    1
                    1
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
            10400565849357983978 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
            }
            10400565850514315339 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
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
            12167572165653230626 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572165713803062 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572165810102506 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166010079205 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166156137114 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166200258440 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166382056893 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166394501094 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166485302750 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166570186518 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166583251908 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166744279257 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166832870156 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166839294852 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572166966433867 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167003951208 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167025734108 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167025868208 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167302697192 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167349016593 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167390952648 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167572892132 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167636003543 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167691424352 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572167767613156 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168282834123 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168340399723 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168436264695 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168439885593 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168513267815 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168543452046 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168557772174 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168570686654 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168593784903 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168671790179 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168677804686 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168764175430 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168772302379 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168789079998 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168805857617 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168926265648 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572168947975617 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572169562717623 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12167572169587904783 = TimeBlendData {
                mTime: f32 = 0.100000001
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
            12910034969924125453 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12910034970175187047 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12910034970342899021 = TimeBlendData {
                mTime: f32 = 0
            }
            12910034970434221611 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12910034970450999230 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028369635287274 = TimeBlendData {
                mTime: f32 = 0
            }
            1300028369835263973 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028370408436676 = TransitionClipBlendData {
                mClipName: hash = "Idle_Run_Trans"
            }
            1300028371461188311 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372087390989 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1300028372338452583 = TimeBlendData {
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
            13039675252671907813 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675254297832151 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675254924034829 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255175096423 = TimeBlendData {
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
            13101179736777342285 = TimeBlendData {
                mTime: f32 = 0
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
            13255853228782025928 = TransitionClipBlendData {
                mClipName: hash = "Spell4_Trans"
            }
            13255853229653279501 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853229904341095 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853229948845454 = TimeBlendData {
                mTime: f32 = 0.5
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
            13630352413652789351 = TimeBlendData {
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
            14022579951088805991 = TimeBlendData {
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
            14094639275747492621 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14094639275998554215 = TimeBlendData {
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
            14777090763081230439 = TimeBlendData {
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
            17417387574496378189 = TimeBlendData {
                mTime: f32 = 0
            }
            17525565602975497549 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238949570624845 = TimeBlendData {
                mTime: f32 = 0
            }
            1789531791005629773 = TimeBlendData {
                mTime: f32 = 0
            }
            18126789362886163789 = TimeBlendData {
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
            2158921754505488487 = TimeBlendData {
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
            4029127110231882952 = TimeBlendData {
                mTime: f32 = 1
            }
            4199991338737384781 = TimeBlendData {
                mTime: f32 = 0
            }
            4564564346258636109 = TimeBlendData {
                mTime: f32 = 0
            }
            4620679766147244266 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
            }
            4620679766347220965 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679766493278874 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679766920393668 = TimeBlendData {
                mTime: f32 = 0
            }
            4620679767303575627 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
            }
            4620679767973145303 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679768599347981 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4620679768850409575 = TimeBlendData {
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
            5312286966566987879 = TimeBlendData {
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
            5692781980495226983 = TimeBlendData {
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
            6030852527244290151 = TimeBlendData {
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
            626268775573227493 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268777199151831 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268777825354509 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            626268778076416103 = TimeBlendData {
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
            6266433748669433829 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433749242606532 = TransitionClipBlendData {
                mClipName: hash = "Idle_Run_Trans"
            }
            6266433749625788491 = TimeBlendData {
                mTime: f32 = 0
            }
            6266433750295358167 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433750921560845 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6266433751172622439 = TimeBlendData {
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
            6391149151793031271 = TimeBlendData {
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
            6427569503800502375 = TimeBlendData {
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
            6463208476702779495 = TimeBlendData {
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
            6521126347080252749 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702301854066283 = TimeBlendData {
                mTime: f32 = 0
            }
            657023860132017092 = TransitionClipBlendData {
                mClipName: hash = "Idle_Run_Trans"
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
            7710673734891841639 = TimeBlendData {
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
            8291053129456789607 = TimeBlendData {
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
            8652687861248336106 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
            }
            8652687862404667467 = TransitionClipBlendData {
                mClipName: hash = "Run_Idle_Trans"
            }
            886425409903181133 = TimeBlendData {
                mTime: f32 = 0
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
            8871152165736523879 = TimeBlendData {
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
            9142213611985938535 = TimeBlendData {
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
        }
    }
}
