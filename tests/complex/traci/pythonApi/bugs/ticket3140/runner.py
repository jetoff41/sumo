#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2008-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Laura Bieker
# @date    2017-05-23
# @version $Id$


from __future__ import print_function
from __future__ import absolute_import
import os
import subprocess
import sys
sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
import traci  # noqa
import sumolib  # noqa

sumoBinary = os.environ["SUMO_BINARY"]
PORT = sumolib.miscutils.getFreeSocketPort()
sumoProcess = subprocess.Popen([sumoBinary,
                                '-c', 'sumo.sumocfg',
                                '--fcd-output', 'fcd.xml',
                                '-S', '-Q',
                                '--remote-port', str(PORT)], stdout=sys.stdout)

traci.init(PORT)
traci.simulationStep()
for i in range(45):
    traci.simulationStep()
traci.vehicle.setSpeedMode("rescue", 7)
traci.vehicle.setSpeed("rescue", 13.9)
traci.trafficlight.setRedYellowGreenState("C", "rrrrrrrrrrrrrrrrrr")
for i in range(21):
    traci.simulationStep()
traci.close()
sumoProcess.wait()
