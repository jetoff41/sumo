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
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--new', '--gui-testing-debug-gl'])

# Change to create edge mode
netedit.createEdgeMode()

# select two-way mode
netedit.changeEditMode('4')

# select chain mode
netedit.changeEditMode('3')

# create a circular road
netedit.leftClick(referencePosition, 300, 150)
netedit.leftClick(referencePosition, 400, 150)
netedit.leftClick(referencePosition, 400, 250)
netedit.leftClick(referencePosition, 400, 350)
netedit.leftClick(referencePosition, 300, 350)
netedit.leftClick(referencePosition, 200, 350)
netedit.leftClick(referencePosition, 200, 250)
netedit.leftClick(referencePosition, 200, 150)
netedit.leftClick(referencePosition, 300, 150)
netedit.cancelEdge()

# disable chain mode
netedit.changeEditMode('3')

# create a complex intersection
netedit.leftClick(referencePosition, 300, 250)
netedit.leftClick(referencePosition, 300, 150)

netedit.leftClick(referencePosition, 300, 250)
netedit.leftClick(referencePosition, 400, 250)

netedit.leftClick(referencePosition, 300, 250)
netedit.leftClick(referencePosition, 300, 350)

netedit.leftClick(referencePosition, 300, 250)
netedit.leftClick(referencePosition, 200, 250)

# rebuild network
netedit.rebuildNetwork()

# Check undo and redo
netedit.undo(referencePosition, 12)
netedit.redo(referencePosition, 12)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
