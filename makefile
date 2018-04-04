cpp_vs_python.png: times_python.csv times_cpp.csv  CatalinaBernal_Graficas.py
	python CatalinaBernal_Graficas.py

gen_times.x :  CatalinaBernal_GenerarTiempos.cpp
	c++ CatalinaBernal_GenerarTiempos.cpp -o tiempo

times_python.csv: CatalinaBernal_GenerarTiempos.py
	python CatalinaBernal_GenerarTiempos.py > times_python.csv

times_cpp.csv: CatalinaBernal_GenerarTiempos.cpp
	c++ CatalinaBernal_GenerarTiempos.cpp -o tiempo
	./tiempo > times_cpp.csv
	
clean:
	rm *.x *.csv *.png
