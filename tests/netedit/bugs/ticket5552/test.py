#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to select mode
netedit.selectMode()

# select junctions
netedit.leftClick(referencePosition, 262, 236)
netedit.leftClick(referencePosition, 392, 236)
netedit.leftClick(referencePosition, 324, 174)
netedit.leftClick(referencePosition, 324, 301)
netedit.leftClick(referencePosition, 262, 301)
netedit.leftClick(referencePosition, 392, 174)

# join junctions
netedit.joinSelectedJunctions()

# rebuild network
netedit.rebuildNetwork()

# split and reconect
netedit.contextualMenuOperation(referencePosition, 324, 236, 12, 0, 0)

# rebuild network
netedit.rebuildNetwork()

# Check undo
netedit.undo(referencePosition, 2)

# rebuild network
netedit.rebuildNetwork()

# Check redo
netedit.redo(referencePosition, 2)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
