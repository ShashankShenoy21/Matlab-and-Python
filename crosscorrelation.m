x = [1 3 5];
y = [2 4 6];
z = fliplr(y);
crossc = conv(x,z);
disp(crossc);
subplot(3,1,1);
stem(x);
xlabel('time');
ylabel('amplitude');
subplot(3,1,2);
stem(z);
xlabel('time');
ylabel('amplitude');
subplot(3,1,3);
stem(crossc);
xlabel('time');
ylabel('amplitude');
title('crosscorrelation');

