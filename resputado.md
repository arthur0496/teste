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

<!-- Ricchard -->
### pc3
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                4
On-line CPU(s) list:   0-3
Thread(s) per core:    1
Core(s) per socket:    4
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 158
Model name:            Intel(R) Core(TM) i5-7300HQ CPU @ 2.50GHz
Stepping:              9
CPU MHz:               1092.725
CPU max MHz:           3500.0000
CPU min MHz:           800.0000
BogoMIPS:              4992.00
Virtualization:        VT-x
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              6144K
NUMA node0 CPU(s):     0-3
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp


## Testes

### teste 1

imagens
-  I1 = trash_on_water
-  I2 = lixo1
-  I1 = lixo2
-  I4 = sunflower

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
|I1|0m0.393s|0m0.400s|0m0.196s|71405568 bytes|
|I2|0m0.428s|0m0.479s|0m0.234s|71479296 bytes|
|I3|0m0.416s|0m0.436s|0m0.270s|71442432 bytes|
|I4|0m0.413s|0m0.426s|0m0.285s|71626752 bytes|

pc3

|image|real|user|sys|memory|
|-----|----|----|---|------|
|I1|0m0.413s|0m0.469s|0m0.234s|70799360 bytes|
|I2|0m0.421s|0m0.411s|0m0.271s|70496256 bytes|
|I3|0m0.321s|0m0.364s|0m0.253s|71016448 bytes|
|I4|0m0.352s|0m0.401s|0m0.265s|70631424 bytes|


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
|I1|0m0.542s|0m0.610s|0m0.229s|78163968 bytes|
|I2|0m0.544s|0m0.600s|0m0.246s|77115392 bytes|
|I3|0m0.545s|0m0.589s|0m0.259s|78065664 bytes|
|I4|0m0.539s|0m0.573s|0m0.251s|78225408 bytes|


pc3
|image|real|user|sys|
|-----|----|----|---|
|I1|0m0.473s|0m0.481s|0m0.296s|77049856 bytes|
|I2|0m0.452s|0m0.490s|0m0.291s|76226560 bytes|
|I3|0m0.445s|0m0.532s|0m0.242s|77266944 bytes|
|I4|0m0.458s|0m0.504s|0m0.278s|77041664 bytes|
