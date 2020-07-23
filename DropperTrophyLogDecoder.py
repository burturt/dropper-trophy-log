#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2020 burturt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys


def printTrophyList(trophyPositiveList, trophyNegativeList):
    """ Prints out trophy list in an easy-to-read way """

    print("---------------------")
    print("\nTrophies submitted:\n")
    if len(trophyPositiveList) == 0:
        print("No trophies submitted. Are you sure you sent the correct list?")
    for element in trophyPositiveList:
        print("- " + element)

    print("\n---------------------\n")

    print("Trophies NOT submitted:\n")
    for element in trophyNegativeList:
        print("- " + element)
    if len(trophyNegativeList) == 0:
        print("All trophies were submitted")

    print("\n---------------------\n")


def decodeUpperRow(upperValue, debug=False):
    """ Decodes the dropper upper row value and returns 2 lists: included and excluded. If returned an empty list,
    the input value is invalid. """

    if not isinstance(upperValue, int):
        if debug:
            print("ERROR: the function must be called with an integer")
        return [], []
    if upperValue >= 1048576:
        if debug:
            print("ERROR: the upper value passed is too large")
        return [], []
    if upperValue < 0:
        if debug:
            print("ERROR: the upper value must be at least 0")
        return [], []

    # Operate on temp variable
    tempUpperValue = upperValue

    # List of trophies at top from 2^0 to 2^19
    trophyUpperList = ["Void Madness", "TTT: Mirrors", "Giant World", "Dragon's Breath", "Arcade Runner", "Trickshot",
                       "Block Stacker", "The Winter is Coming", "Arrrrggg Matey", "Fun House", "Staff Meeting",
                       "Temple Jump", "Hot Swirl", "Number 2", "Choose carefully", "Focus Pocus", "MI",
                       "Frank's Revenge TROPHY", "Learning to Fly Part 2", "Nostalgiamon"]

    # positive = they submitted it, negative = they did not submit it
    positiveTrophy = []
    negativeTrophy = []

    for basePower in range(19, -1, -1):
        if tempUpperValue - (2 ** basePower) >= 0:
            positiveTrophy.append(trophyUpperList[basePower])
            tempUpperValue -= (2 ** basePower)
        else:
            negativeTrophy.append(trophyUpperList[basePower])

    return positiveTrophy, negativeTrophy


def decodeLowerRow(lowerValue, debug=False):
    """ Decodes the dropper lower row value and returns 2 lists: included and excluded. If returned an empty list,
    the input value is invalid. """

    if not isinstance(lowerValue, int):
        if debug:
            print("ERROR: the function must be called with an integer")
        return [], []
    if lowerValue >= 1048576:
        if debug:
            print("ERROR: the upper value passed is too large")
        return [], []
    if lowerValue < 0:
        if debug:
            print("ERROR: the upper value must be at least 0")
        return [], []

    # Operate on temp variable
    tempLowerValue = lowerValue

    # List of trophies at bottom from 2^0 to 2^19
    trophyUpperList = ["OIT", "TTT: Unstable Mineshaft", "TTT: Evil Pumpkin", "Down the Chimney We Go", "Decrescendo",
                       "Ballad of Frank", "Spodermin", "Pickles", "The Cave", "Wooly Mess", "H-E Double Hockey Sticks",
                       "Computer Time", "Teeny Tiny You", "Lava Pit", "Parkour Plunge", "Pathway Peril",
                       "Threading The Needle", "Bright Idea", "Learning to Fly (1)", "Frank's Revenge HELMET"]

    # positive = they submitted it, negative = they did not submit it
    positiveTrophy = []
    negativeTrophy = []

    for basePower in range(19, -1, -1):
        if tempLowerValue - (2 ** basePower) >= 0:
            positiveTrophy.append(trophyUpperList[basePower])
            tempLowerValue -= (2 ** basePower)
        else:
            negativeTrophy.append(trophyUpperList[basePower])

    return positiveTrophy, negativeTrophy


if __name__ == "__main__":

    if len(sys.argv) != 3 and len(sys.argv) > 1:
        print("Invalid # of arguments")
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " UpperTrophyValue LowerTrophyValue")
        print("Ex: " + sys.argv[0] + " 2643 1048575")
        exit(1)

    positiveTrophyTempList1, negativeTrophyTempList1 = decodeUpperRow(int(sys.argv[1]), True)
    positiveTrophyTempList2, negativeTrophyTempList2 = decodeLowerRow(int(sys.argv[2]), True)

    if len(positiveTrophyTempList1) == 0 and len(negativeTrophyTempList1) == 0:
        print("Upper row value invalid")
        exit(1)
    if len(positiveTrophyTempList2) == 0 and len(negativeTrophyTempList2) == 0:
        print("Lower row value invalid")
        exit(1)

    positiveTrophyTempList = positiveTrophyTempList1 + positiveTrophyTempList2
    negativeTrophyTempList = negativeTrophyTempList1 + negativeTrophyTempList2

    positiveTrophyTempList.sort()
    negativeTrophyTempList.sort()

    printTrophyList(positiveTrophyTempList, negativeTrophyTempList)
