# -*- coding: utf-8 -*-

#Copyright 2016-2018 Angel Ferran Pousa, DESY
#
#This file is part of VisualPIC.
#
#VisualPIC is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#VisualPIC is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with VisualPIC.  If not, see <http://www.gnu.org/licenses/>.

from VisualPIC.DataReading.dataReaderSelectors import RawDataReaderSelector

class RawDataTags(object):
    def __init__(self, simulationCode, name, location, timeSteps, speciesName = "", internalName = ""):
        self.dataName = name
        self.dataLocation = location
        self.speciesName = speciesName
        self.timeSteps = timeSteps
        self.dataReader = RawDataReaderSelector.GetReader(simulationCode, location, speciesName, name, internalName, timeSteps[0])

    def GetTimeSteps(self):
        return self.timeSteps

    def GetTags(self, timeStep):
        return self.dataReader.GetData(timeStep)