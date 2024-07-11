#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Yasuo/Skins/Skin0/Particles/Yasuo_Base_R_tar_imp_01" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 120
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    10
                }
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            IsLocalSpace: bool = false
                            Acceleration: embed = ValueVector3 {
                                ConstantValue: vec3 = { 0, -400, 0 }
                            }
                        }
                    }
                    FieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {
                            Radius: embed = ValueFloat {
                                ConstantValue: f32 = 1000
                            }
                            Strength: embed = ValueFloat {
                                ConstantValue: f32 = 3
                                Dynamics: pointer = VfxAnimatedFloatVariableData {
                                    ProbabilityTables: list[pointer] = {
                                        VfxProbabilityTableData {
                                            KeyTimes: list[f32] = {
                                                0
                                                1
                                            }
                                            KeyValues: list[f32] = {
                                                0.75
                                                1.5
                                            }
                                        }
                                    }
                                    Times: list[f32] = {
                                        0
                                    }
                                    Values: list[f32] = {
                                        3
                                    }
                                }
                            }
                        }
                    }
                }
                EmitterName: string = "sparks"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    1
                                    4
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 50, 0, 0 }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
                                ProbabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        KeyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        KeyValues: list[f32] = {
                                            0
                                            120
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
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-firemissile.dds"
                MeshRenderFlags: u8 = 0
                ColorLookUpTypeY: u8 = 3
                ColorLookUpScales: vec2 = { 1, 0.5 }
                ColorLookUpOffsets: vec2 = { 0, 0.5 }
                IsUniformScale: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 12, 12, 12 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.300000012
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
                            { 12, 12, 12 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_FireHit.dds"
                StartFrame: u16 = 1
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 100
                }
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
                                    0.5
                                    1
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
                    10
                }
                Lifetime: option[f32] = {
                    1
                }
                Period: option[f32] = {
                    1
                }
                TimeActiveDuringPeriod: option[f32] = {
                    0.0500000007
                }
                EmitterName: string = "flame"
                Importance: u8 = 2
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    Flags: u8 = 1
                    Size: vec3 = { 5, 5, 5 }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 20, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-incinerate.dds"
                MeshRenderFlags: u8 = 0
                ColorLookUpTypeY: u8 = 3
                ColorLookUpScales: vec2 = { 1, 0.449999988 }
                ColorLookUpOffsets: vec2 = { 0, 0.550000012 }
                IsUniformScale: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 165, 165, 165 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.300000012
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
                            { 165, 165, 165 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.600000024, 0.600000024, 0.600000024 }
                            { 1.10000002, 1.10000002, 1.10000002 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_FireHit.dds"
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 10
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    1
                }
                IsSingleParticle: flag = true
                EmitterName: string = "sparks_02"
                Importance: u8 = 2
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 50, 0, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-incinerate.dds"
                MeshRenderFlags: u8 = 0
                ColorLookUpTypeY: u8 = 3
                ColorLookUpScales: vec2 = { 1, 0.150000006 }
                ColorLookUpOffsets: vec2 = { 0, 0.800000012 }
                IsUniformScale: flag = true
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 121, 121, 121 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.800000012
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 121, 121, 121 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_FireHit.dds"
                StartFrame: u16 = 2
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 145
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.400000006
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.349999994
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    10
                }
                Lifetime: option[f32] = {
                    0.125
                }
                EmitterLinger: option[f32] = {
                    1.5
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            IsLocalSpace: bool = false
                            Acceleration: embed = ValueVector3 {
                                ConstantValue: vec3 = { 0, -500, 0 }
                            }
                        }
                    }
                }
                EmitterName: string = "magic_sparks"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 275, 275, 275 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1.54999995
                                    0.25
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 275, 275, 275 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[f32] = {
                            1
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 20, 20, 20 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
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
                                        3
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            Times: list[f32] = {
                                0
                            }
                            Values: list[vec3] = {
                                { 20, 20, 20 }
                            }
                        }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 30, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-smoke32_07.dds"
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 100, 100 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.25
                                    0.850000024
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 100, 100 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_Flare-Rainbow_purp_01.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 80
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.300000012
                }
                ParticleLinger: option[f32] = {
                    10
                }
                Lifetime: option[f32] = {
                    0.150000006
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            IsLocalSpace: bool = false
                            Acceleration: embed = ValueVector3 {
                                ConstantValue: vec3 = { 0, -2250, 0 }
                            }
                        }
                    }
                }
                EmitterName: string = "molten_rock_02"
                Importance: u8 = 2
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 1050, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 1050, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
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
                                        40
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
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 50, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-hold.dds"
                BlendMode: u8 = 1
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1000
                                    1000
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
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 10.5, 10.5, 10.5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.850000024
                                    1.10000002
                                    2.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 10.5, 10.5, 10.5 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_DirtBits_03.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 500
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    0.400000006
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {}
                Lifetime: option[f32] = {
                    0.300000012
                }
                FieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    FieldAccelerationDefinitions: list[embed] = {
                        VfxFieldAccelerationDefinitionData {
                            IsLocalSpace: bool = false
                        }
                    }
                    FieldDragDefinitions: list[embed] = {
                        VfxFieldDragDefinitionData {}
                    }
                }
                EmitterName: string = "followsparks"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 480, 0 }
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
                            { 0, 480, 0 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[f32] = {
                            0.600000024
                            -1.0666666
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 60, 0, 0 }
                    }
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 0, 1.00000012 }
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 150, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-sparks.dds"
                MeshRenderFlags: u8 = 0
                ColorLookUpScales: vec2 = { 0.5, 1 }
                ColorLookUpOffsets: vec2 = { 0.5, 0 }
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
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 50, 50, 50 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.100000001
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
                            { 50, 50, 50 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_Fireball_hit.dds"
                NumFrames: u16 = 4
                StartFrame: u16 = 2
                TexDiv: vec2 = { 2, 3 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.100000001
                }
                ParticleLinger: option[f32] = {
                    10
                }
                Lifetime: option[f32] = {
                    0.100000001
                }
                IsSingleParticle: flag = true
                EmitterName: string = "flat"
                Importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 80, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleBirthScaleByBoundObjectSize: f32 = 0.5
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_color-rampdown.dds"
                MeshRenderFlags: u8 = 0
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 5, 5, 5 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.899999976
                                    1.20000005
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 5, 5, 5 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/common_Flare-Sun_17.dds"
            }
        }
        ParticleName: string = "Yasuo_Base_R_tar_imp_01"
        ParticlePath: string = "Characters/Yasuo/Skins/Skin0/Particles/Yasuo_Base_R_tar_imp_01"
        Flags: u16 = 134
    }
    "Characters/Yasuo/Skins/Skin0/Particles/Yasuo_Base_Q_wind_mis" = VfxSystemDefinitionData {
        ComplexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 15
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    0.600000024
                }
                EmitterName: string = "tornado"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.600000024
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 100, 100 }
                        }
                    }
                }
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/yasuo_base_e_big_tonado.scb"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Color_yasuo_w_windwall_dust.dds"
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.67839998, 0.944999993, 1, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.330000013
                            0.660000026
                            1
                        }
                        Values: list[vec4] = {
                            { 0.67839998, 0.944999993, 1, 0 }
                            { 0.67839998, 0.944999993, 1, 0.75 }
                            { 1, 1, 1, 0.75 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 100
                ColorLookUpTypeY: u8 = 3
                DisableBackfaceCull: bool = true
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                                    0.5
                                    1.25
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
                            { 1, 500, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.330000013
                                0.660000026
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.75
                                0.5
                                0.25
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.150000006
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin0/Yasuo_Skin45_Generic_Noise.dds"
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.75, 2.5, 1.75 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 1.75, 2.5, 1.75 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.119999997
                            0.25
                        }
                        Values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1, 1, 1 }
                            { 1.14999998, 1.14999998, 1.14999998 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_base_Q_tonado_wind_cas.dds"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 2, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    0.200000003
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 2, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 15
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    0.600000024
                }
                EmitterName: string = "tornado_shape"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/yasuo_base_e_big_tonado_shape.scb"
                    }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Color_Yasuo_Base_E_tonado_blend.dds"
                BlendMode: u8 = 4
                BirthColor: embed = ValueColor {
                    ConstantValue: vec4 = { 0.67839998, 0.944999993, 1, 1 }
                }
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.330000013
                            0.660000026
                            1
                        }
                        Values: list[vec4] = {
                            { 0.67839998, 0.944999993, 1, 0 }
                            { 0.67839998, 0.944999993, 1, 0.75 }
                            { 1, 1, 1, 0.75 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = 100
                ColorLookUpTypeY: u8 = 3
                DisableBackfaceCull: bool = true
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.330000013
                                0.660000026
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.75
                                0.5
                                0.25
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.150000006
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin0/Yasuo_Skin45_Generic_Noise.dds"
                }
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 200, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                                    0.75
                                    1.25
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
                            { 1, 200, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.70000005, 2.5, 1.70000005 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1.70000005, 2.5, 1.70000005 }
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
                            { 0.25, 0.25, 0.25 }
                            { 1.75, 1.75, 1.75 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_base_E_tonado.dds"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 1, 0 }
                    Dynamics: pointer = VfxAnimatedVector2fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0
                                    0.200000003
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 20
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                }
                ParticleLinger: option[f32] = {
                    10.5
                }
                Lifetime: option[f32] = {
                    0.75
                }
                EmitterName: string = "ground_shape"
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                BlendMode: u8 = 1
                Color: embed = ValueColor {
                    Dynamics: pointer = VfxAnimatedColorVariableData {
                        Times: list[f32] = {
                            0
                            0.0500000007
                            1
                        }
                        Values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                Pass: i16 = -90
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 90, 1, 90 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 90, 1, 90 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 140, 140, 0 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        Values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_Q_tornado_ground_shape_cas.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 80
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.699999988
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.400000006
                                    0.75
                                    2
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    1
                }
                Lifetime: option[f32] = {
                    2
                }
                EmitterName: string = "rock"
                BirthOrbitalVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 2, 0 }
                }
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    250
                                    500
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, 1300, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 650, 0 }
                            { 0, 1950, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 0 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        -100
                                        100
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
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/yasuo_base_q_ground_rock.scb"
                    }
                }
                BlendMode: u8 = 3
                DisableBackfaceCull: bool = true
                DoesCastShadow: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -20
                                    20
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -20
                                    20
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 300, 300, 300 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.5, 1.25, 1.25 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.25
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.25
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.25
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0.5, 1.25, 1.25 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.0500000007
                            0.400000006
                            1
                        }
                        Values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_base_Q_ground_rock_mis.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 400
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.5
                                    0.699999988
                                    2
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
                    11
                }
                Lifetime: option[f32] = {
                    0.699999988
                }
                EmitterName: string = "ground_dirt"
                BirthVelocity: embed = ValueVector3 {
                    ConstantValue: vec3 = { 100, 300, 600 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -2
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.200000003
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 100, 300, 600 }
                        }
                    }
                }
                WorldAcceleration: embed = IntegratedValueVector3 {
                    ConstantValue: vec3 = { 0, -1000, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0, -1000, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
                        ConstantValue: vec3 = { 1, 0, 0 }
                        Dynamics: pointer = VfxAnimatedVector3fVariableData {
                            ProbabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    KeyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    KeyValues: list[f32] = {
                                        -50
                                        50
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
                }
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Color_Yasuo_Q_wind.dds"
                BlendMode: u8 = 1
                ParticleIsLocalOrientation: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 1, 1 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    -1000
                                    1000
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 20, 20, 20 }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_Base_Q_ground_dirt_mis.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                TimeBeforeFirstEmission: f32 = 0.100000001
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 2
                }
                ParticleLinger: option[f32] = {
                    3
                }
                Lifetime: option[f32] = {
                    0.5
                }
                EmitterName: string = "ground_crack"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 80, -50, 0 }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Color_yasuo_w_windwall_dust.dds"
                BlendMode: u8 = 1
                Pass: i16 = -1000
                ColorLookUpTypeY: u8 = 3
                MiscRenderFlags: u8 = 1
                IsGroundLayer: flag = true
                UseNavmeshMask: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 10 }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 30, 165, 0 }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_base_q_groud_crack.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 80
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.5
                    Dynamics: pointer = VfxAnimatedFloatVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                KeyValues: list[f32] = {
                                    0.300000012
                                    0.5
                                    1
                                }
                            }
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[f32] = {
                            0.5
                        }
                    }
                }
                ParticleLinger: option[f32] = {
                    10
                }
                Lifetime: option[f32] = {
                    1
                }
                EmitterName: string = "ground_base"
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    EmitOffset: embed = ValueVector3 {
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
                                        50
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
                    EmitRotationAngles: list[embed] = {
                        ValueFloat {
                            ConstantValue: f32 = 1
                            Dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                Times: list[f32] = {
                                    0
                                }
                                Values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    EmitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                Primitive: pointer = VfxPrimitiveArbitraryQuad {}
                ParticleColorTexture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Color_Yasuo_base_E_inner_wind.dds"
                BlendMode: u8 = 1
                Pass: i16 = -70
                MeshRenderFlags: u8 = 0
                ColorLookUpTypeY: u8 = 3
                IsUniformScale: flag = true
                IsRandomStartFrame: flag = true
                BirthRotation0: embed = ValueVector3 {
                    ConstantValue: vec3 = { -90, 1, 0 }
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
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { -90, 1, 0 }
                        }
                    }
                }
                IsLocalOrientation: flag = false
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0.25, 0.25, 0.25 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                KeyTimes: list[f32] = {
                                    0
                                    1
                                }
                                KeyValues: list[f32] = {
                                    50
                                    200
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 0.25, 0.25, 0.25 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_E_dash_smoke.dds"
                NumFrames: u16 = 4
                TexDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 1.25
                }
                ParticleLinger: option[f32] = {
                    10.75
                }
                Lifetime: option[f32] = {
                    1.20000005
                }
                IsSingleParticle: flag = true
                EmitterName: string = "distort_large"
                Importance: u8 = 0
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    ConstantValue: vec3 = { 0, 0, 0 }
                }
                ParticleColorTexture: string = "ASSETS/Characters/Garen/Skins/Base/Particles/Garen_color-rampdown32.dds"
                BlendMode: u8 = 1
                Pass: i16 = 1000
                MeshRenderFlags: u8 = 0
                DistortionDefinition: pointer = VfxDistortionDefinitionData {
                    Distortion: f32 = 0.5
                    DistortionMode: u8 = 2
                    NormalMapTexture: string = "ASSETS/Characters/Garen/Skins/Base/Particles/Garen_distort-soft-shockwave.dds"
                }
                MiscRenderFlags: u8 = 1
                IsUniformScale: flag = true
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 300, 300, 300 }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                            1
                        }
                        Values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Garen/Skins/Base/Particles/Garen_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 25
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    1.20000005
                }
                EmitterName: string = "slash1"
                BindWeight: embed = ValueFloat {
                    ConstantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_basic_attack_mesh_01.sco"
                    }
                }
                BlendMode: u8 = 4
                DisableBackfaceCull: bool = true
                ParticleIsLocalOrientation: flag = true
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                                    0.5
                                    1.25
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
                            { 1, 500, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.75, 2.5, 1.75 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 1.75, 2.5, 1.75 }
                        }
                    }
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.330000013
                                0.660000026
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.75
                                0.5
                                0.25
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.150000006
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin0/Yasuo_Skin45_Generic_Noise.dds"
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.119999997
                            0.25
                        }
                        Values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1, 1, 1 }
                            { 1.14999998, 1.14999998, 1.14999998 }
                        }
                    }
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_Basic_attack_trail2.dds"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -3.0999999, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 25
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    1.20000005
                }
                EmitterName: string = "slash2"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_basic_attack_mesh_01.sco"
                    }
                }
                BlendMode: u8 = 4
                DisableBackfaceCull: bool = true
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                                    0.5
                                    1.25
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
                            { 1, 500, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.75, 2.5, 1.75 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 1.75, 2.5, 1.75 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.119999997
                            0.25
                        }
                        Values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1, 1, 1 }
                            { 1.14999998, 1.14999998, 1.14999998 }
                        }
                    }
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.330000013
                                0.660000026
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.75
                                0.5
                                0.25
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.150000006
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin0/Yasuo_Skin45_Generic_Noise.dds"
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_Basic_attack_trail2.dds"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { 3.5, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
            }
            VfxEmitterDefinitionData {
                Rate: embed = ValueFloat {
                    ConstantValue: f32 = 25
                }
                ParticleLifetime: embed = ValueFloat {
                    ConstantValue: f32 = 0.25
                }
                Lifetime: option[f32] = {
                    0.600000024
                }
                EmitterName: string = "slash3"
                0x3bf0b4ed: pointer = 0xee39916f {
                    EmitOffset: vec3 = { 0, 0, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    ScaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                Primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_basic_attack_mesh_01.sco"
                    }
                }
                BlendMode: u8 = 4
                DisableBackfaceCull: bool = true
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
                            VfxProbabilityTableData {}
                        }
                        Times: list[f32] = {
                            0
                        }
                        Values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                BirthRotationalVelocity0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1, 500, 0 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
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
                                    0.5
                                    1.25
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
                            { 1, 500, 0 }
                        }
                    }
                }
                BirthScale0: embed = ValueVector3 {
                    ConstantValue: vec3 = { 1.75, 2.5, 1.75 }
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        ProbabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 1.75, 2.5, 1.75 }
                        }
                    }
                }
                Scale0: embed = ValueVector3 {
                    Dynamics: pointer = VfxAnimatedVector3fVariableData {
                        Times: list[f32] = {
                            0
                            0.119999997
                            0.25
                        }
                        Values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1, 1, 1 }
                            { 1.14999998, 1.14999998, 1.14999998 }
                        }
                    }
                }
                AlphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    ErosionDriveCurve: embed = ValueFloat {
                        Dynamics: pointer = VfxAnimatedFloatVariableData {
                            Times: list[f32] = {
                                0
                                0.330000013
                                0.660000026
                                1
                            }
                            Values: list[f32] = {
                                1
                                0.75
                                0.5
                                0.25
                            }
                        }
                    }
                    ErosionFeatherIn: f32 = 0.150000006
                    ErosionFeatherOut: f32 = 0.150000006
                    ErosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin0/Yasuo_Skin45_Generic_Noise.dds"
                }
                Texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Particles/Yasuo_Basic_attack_trail2.dds"
                UvMode: u8 = 2
                BirthUvScrollRate: embed = ValueVector2 {
                    ConstantValue: vec2 = { -3.5, 0 }
                }
                BirthUvoffset: embed = ValueVector2 {
                    ConstantValue: vec2 = { -1, 1 }
                }
            }
        }
        ParticleName: string = "Yasuo_Base_Q_wind_mis"
        ParticlePath: string = "Characters/Yasuo/Skins/Skin0/Particles/Yasuo_Base_Q_wind_mis"
        SoundOnCreateDefault: string = "Play_sfx_Yasuo_YasuoQ3W_missilelaunch"
    }
}
