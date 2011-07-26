#This file is part of QuTiP.
#
#    QuTIP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#    QuTIP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with QuTIP.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2011, Paul D. Nation & Robert J. Johansson
#
###########################################################################
import sys,os
import examples
from examples import exconfig
from scipy import arange,array,any
def demos():
    if os.environ['QUTIP_GRAPHICS']=='YES':
        from gui import Examples
        if os.environ['QUTIP_GUI']=="PYSIDE":
            from PySide import QtGui, QtCore
        elif os.environ['QUTIP_GUI']=="PYQT4":
            from PyQt4 import QtGui, QtCore
        def start_gui():
            app=QtGui.QApplication.instance()#checks if QApplication already exists (needed for iPython)
            if not app:#create QApplication if it doesnt exist
                app = QtGui.QApplication(sys.argv)
            gui=Examples()
            gui.show()
            gui.raise_()
            app.exec_()
    else:
        opts=array([123456,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45])
        lopts=arange(len(opts))
    exconfig.option=0

    while exconfig.option<123456:
        exconfig.option=123456
        if os.environ['QUTIP_GRAPHICS']=='YES':
            start_gui()
        else:
            if sys.stdout.isatty():
                print '-'*80
                print '\nQuTiP Example Scripts:'
                print '-----------------------'
                print '[1]  Basic Obj operations'
                print '[2]  Operator usage examples'
                print '[3]  Tensor / partial trace usage'
                print '[4]  Wigner & Q dist. of Schrodinger cat-state'
                print '[5]  Squeezed state'
                print '[6]  Steady-state cavity+qubit'
                print '[7]  Steady-state oscillator in thermal bath'
                print '[8]  None'
                print '[9]  None'
                print '[10] None'
                print '[11] None'
                print '[12] None'
                print '[13] Heisenberg spin-chain (N=4)'
                print '[14] None'
                print '[15] Qubit decay on the Bloch sphere'
                print '[16] None'
                print '[17] None'
                print '[18] None'
                print '[19] None'
                print '[20] None'
                print '[0]  Exit...'
                wflag=0
                while wflag<3:
                    userinpt=raw_input("\nPick an example to run:")
                    try:
                        userinpt=int(userinpt)
                    except:
                        print 'Invalid choice.  Please pick again.'
                        wflag+=1
                    else:
                        if any(userinpt==lopts):
                            exconfig.option=opts[userinpt]
                            break
                        else:
                            print 'Invalid choice.  Please pick again.'
                            wflag+=1
                if wflag==3:
                    print ('\nThird time was not a charm in your case.')
                    print('It seems you cannot pick a valid option...\n')
                    return
            else:
                raise TypeError('Demos must be run from the terminal if no GUI is avaliable.')
        if exconfig.option==11:
            examples.qobjbasics()
        elif exconfig.option==12:
            pass
        elif exconfig.option==13:
            examples.tensorptrace()
        elif exconfig.option==14:
            examples.schrodingercat()
        elif exconfig.option==15:
            examples.squeezed()
        elif exconfig.option==21:
            examples.cqsteady()
        elif exconfig.option==22:
            examples.thermalss()
        elif exconfig.option==23:
            pass
        elif exconfig.option==24:
            examples.jc_vacuum_rabi()
        elif exconfig.option==25:
            examples.jc_lasing()
            pass
        elif exconfig.option==31:
            pass
        elif exconfig.option==32:
            pass
        elif exconfig.option==33:
            examples.spinchain()
        elif exconfig.option==34:
            examples.correlation()
        elif exconfig.option==35:
            examples.blochdemo()
        elif exconfig.option==41:
            examples.cavityqubitmc()
        elif exconfig.option==42:
            examples.trilinearmc()   
        elif exconfig.option==43:
            examples.mcthermal()
        elif exconfig.option==44:
            examples.td_rabi()
        elif exconfig.option==45:
            pass
            
            
            
