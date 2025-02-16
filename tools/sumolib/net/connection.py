# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2011-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    connection.py
# @author  Daniel Krajzewicz
# @author  Laura Bieker
# @author  Karol Stosiek
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2011-11-28
# @version $Id$


class Connection:
    # constants as defined in sumo/src/utils/xml/SUMOXMLDefinitions.cpp
    LINKDIR_STRAIGHT = "s"
    LINKDIR_TURN = "t"
    LINKDIR_LEFT = "l"
    LINKDIR_RIGHT = "r"
    LINKDIR_PARTLEFT = "L"
    LINKDIR_PARTRIGHT = "R"

    """edge connection for a sumo network"""

    def __init__(self, fromEdge, toEdge, fromLane, toLane, direction, tls, tllink, state, viaLaneID=None):
        self._from = fromEdge
        self._to = toEdge
        self._fromLane = fromLane
        self._toLane = toLane
        self._direction = direction
        self._tls = tls
        self._tlLink = tllink
        self._state = state
        self._via = viaLaneID
        self._params = {}

    def __str__(self):
        return '<connection from="%s" to="%s" fromLane="%s" toLane="%s" %sdirection="%s">' % (
            self._from.getID(),
            self._to.getID(),
            self._fromLane.getIndex(),
            self._toLane.getIndex(),
            ('' if self._tls == '' else 'tl="%s" linkIndex="%s" ' %
             (self._tls, self._tlLink)),
            self._direction)

    def setParam(self, key, value):
        self._params[key] = value

    def getParam(self, key, default=None):
        return self._params.get(key, default)

    def getParams(self):
        return self._params

    def getFrom(self):
        return self._fromLane.getEdge()

    def getTo(self):
        return self._toLane.getEdge()

    def getFromLane(self):
        return self._fromLane

    def getToLane(self):
        return self._toLane

    def getViaLaneID(self):
        return self._via

    def getDirection(self):
        return self._direction

    def getTLSID(self):
        return self._tls

    def getTLLinkIndex(self):
        return self._tlLink

    def getJunctionIndex(self):
        return self._from.getToNode().getLinkIndex(self)

    def getJunction(self):
        return self._from.getToNode()

    def getState(self):
        return self._state
