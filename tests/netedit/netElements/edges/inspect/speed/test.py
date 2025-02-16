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

# go to inspect mode
netedit.inspectMode()

# inspect edge
netedit.leftClick(referencePosition, 250, 180)

# Change parameter 3 with a non valid value (empty speed)
netedit.modifyAttribute(3, "", False)

# Change parameter 3 with a non valid value (dummy speed)
netedit.modifyAttribute(3, "dummySpeed", False)

# Change parameter 3 with a non valid value (negative speed)
netedit.modifyAttribute(3, "-13", False)

# Change parameter 3 with a valid value
netedit.modifyAttribute(3, "120.5", False)

# recompute
netedit.rebuildNetwork()

# Check undo
netedit.undo(referencePosition, 1)

# recompute
netedit.rebuildNetwork()

# Check redo
netedit.redo(referencePosition, 1)

# save additionals
netedit.saveAdditionals(referencePosition)

# save network
netedit.saveNetwork(referencePosition)

# quit netedit
netedit.quit(neteditProcess)
