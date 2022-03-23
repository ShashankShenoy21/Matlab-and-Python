N = 2;
Wc = 800;
FS = 8000;
wc = 2*pi*Wc/FS;
T = 1;
[a, b] = butter(N, wc, 's');
[ad, bd] = bilinear(a, b, T);
freqz(ad,bd,512,8000); 
axis([0 4000 -40 1]);
title('Frequency Response of the Filter')