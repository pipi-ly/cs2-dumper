'''
Created using https://github.com/a2x/cs2-dumper
Fri, 17 Nov 2023 03:37:55 +0000
'''

class client_dll: # client.dll
    dwEntityList = 0x17B0D00
    dwForceAttack = 0x16B5410
    dwForceAttack2 = 0x16B54A0
    dwForceBackward = 0x16B56E0
    dwForceCrouch = 0x16B59B0
    dwForceForward = 0x16B5650
    dwForceJump = 0x16B5920
    dwForceLeft = 0x16B5770
    dwForceRight = 0x16B5800
    dwGameEntitySystem = 0x18DC3E0
    dwGameEntitySystem_getHighestEntityIndex = 0x1510
    dwGameRules = 0x180C9B0
    dwGlobalVars = 0x16B14F0
    dwGlowManager = 0x180C9D8
    dwInterfaceLinkList = 0x190A078
    dwLocalPlayerController = 0x1800018
    dwLocalPlayerPawn = 0x16BC4B8
    dwPlantedC4 = 0x1813F78
    dwPrediction = 0x16BC380
    dwSensitivity = 0x180DF68
    dwSensitivity_sensitivity = 0x40
    dwViewAngles = 0x186FFC0
    dwViewMatrix = 0x180F340
    dwViewRender = 0x180FBC0

class engine2_dll: # engine2.dll
    dwBuildNumber = 0x48A514
    dwNetworkGameClient = 0x489AC0
    dwNetworkGameClient_getLocalPlayer = 0xF0
    dwNetworkGameClient_maxClients = 0x250
    dwNetworkGameClient_signOnState = 0x240
    dwWindowHeight = 0x540CE4
    dwWindowWidth = 0x540CE0

class inputsystem_dll: # inputsystem.dll
    dwInputSystem = 0x35760
