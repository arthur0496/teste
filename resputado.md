Testes:

## Participantes

<!-- alax -->
### pc1
- Architecture:          x86_64
- CPU op-mode(s):        32-bit, 64-bit
- Byte Order:            Little Endian
- CPU(s):                4
- On-line CPU(s) list:   0-3
- Thread(s) per core:    2
- Core(s) per socket:    2
- Socket(s):             1
- NUMA node(s):          1
- Vendor ID:             GenuineIntel
- CPU family:            6
- Model:                 42
- Model name:            Intel(R) Core(TM) i3-2377M CPU @ - 1.50GHz
- Stepping:              7
- CPU MHz:               898.366
- CPU max MHz:           1500,0000
- CPU min MHz:           800,0000
- BogoMIPS:              2993.06
- Virtualization:        VT-x
- L1d cache:             32K
- L1i cache:             32K
- L2 cache:              256K
- L3 cache:              3072K
- NUMA node0 CPU(s):     0-3

<!-- arthur -->
### pc3
- Architecture:          x86_64
- CPU op-mode(s):        32-bit, 64-bit
- Byte Order:            Little Endian
- CPU(s):                4
- On-line CPU(s) list:   0-3
- Thread(s) per core:    2
- Core(s) per socket:    2
- Socket(s):             1
- NUMA node(s):          1
- Vendor ID:             GenuineIntel
- CPU family:            6
- Model:                 142
- Model name:            Intel(R) Core(TM) i5-7200U CPU @ - 2.50GHz
- Stepping:              9
- CPU MHz:               500.898
- CPU max MHz:           3100,0000
- CPU min MHz:           400,0000
- BogoMIPS:              5424.00
- Virtualization:        VT-x
- L1d cache:             32K
- L1i cache:             32K
- L2 cache:              256K
- L3 cache:              3072K
- NUMA node0 CPU(s):     0-3

## Testes

### teste 1

imagens
-  I1 = trash_on_water
-  I2 = lixo2
-  I1 = lixo3
-  I1 = sunflower

pc1 

|image|real|user|sys|
|-----|----|----|---|
|I1|0m1.501s|0m0.944s|0m0.501s|
|I2|0m0.917s|0m1.012s|0m0.443s|
|I3|0m0.913s|0m1.044s|0m0.408s|
|I4|0m1.078s|0m1.113s|0m0.512s|

pc2

|image|real|user|sys|
|-----|----|----|---|
|I1|0m0.519s|0m0.459s|0m0.060s|
|I2|0m0.405s|0m0.371s|0m0.036s|
|I3|0m0.383s|0m0.323s|0m0.062s|
|I4|0m0.383s|0m0.323s|0m0.062s|


### teste 2


pc1

|image|real|user|sys|
|-----|----|----|---|
|I1|0m2.102s|0m1.946s|0m0.740s|
|I2|0m1.719s|0m1.737s|0m0.824s|
|I3|0m1.749s|0m1.922s|0m0.747s|
|I4|0m2.243s|0m2.660s|0m0.749s|

pc2
|image|real|user|sys|
|-----|----|----|---|
|I1|0m0.699s|0m0.742s|0m0.068s|
|I2|0m0.690s|0m0.726s|0m0.056s|
|I3|0m0.738s|0m0.799s|0m0.053s|
|I4|0m0.874s|0m1.103s|0m0.069s|


## teste 1 420
pc2
|image|real|user|sys|
|-----|----|----|---|
|I1|0m0.506s|0m0.451s|0m0.057s|
|I2|
|I3|
|I4|