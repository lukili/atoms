all:
	sudo python3 setup.py install
	sudo pip3 install --upgrade .
                    
dependencies:
	sudo -H pip3 install numpy
	sudo -H pip3 install scipy
	sudo -H pip3 install mpi4py
	sudo -H pip3 install ase
	sudo -H pip3 install cython
	
clean:
	#sudo rm -r build
	#sudo rm -r dist
	#sudo rm -r btom.egg*
	
