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

# recompute
netedit.rebuildNetwork()

# toogle select lanes
netedit.changeEditMode('2')

# go to inspect mode
netedit.inspectMode()

# inspect edge
netedit.leftClick(referencePosition, 250, 180)

# Change parameter 1 with an non valid value (dummy)
netedit.modifyAttribute(2, "DummyAllowed", False)

# Change parameter 1 with a valid value (empty)
netedit.modifyAttribute(2, "", False)

# Change parameter 1 with a valid value (different separators)
netedit.modifyAttribute(2, "authority  army, passenger; taxi. tram", False)

# Change parameter 1 with a valid value (empty)
netedit.modifyAttribute(2, "", False)

# Change parameter 1 with a valid value (empty)
netedit.modifyAttribute(2, "authority army vip passenger hov taxi bus coach tram bicycle", False)

# recompute
netedit.rebuildNetwork()

# Check undos
netedit.undo(referencePosition, 1)

# recompute
netedit.rebuildNetwork()

# check redos
netedit.redo(referencePosition, 1)

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
