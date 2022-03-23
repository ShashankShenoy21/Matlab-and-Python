clear all;
close all;
x = input('Enter the value of the first function x[n] :'); %taking user input for second function x[n]
y = input('Enter the value of the second function y[n] :'); %taking user input for second function y[n]
computation (x,y);




function computation (x,y)
disp('Function x[n]:'); disp(x); %dispalying the value of x[n]
disp('Function y[n]:'); disp(y); %displaying the value of y[n]
subplot(6,1,1);
plot(x); %plot the function x[n]
xlabel('n'); ylabel('x');
title('x[n]');
subplot(6,1,2);
plot(y); %plot the function y[n]
xlabel('n'); ylabel('y');
title('y[n]');
X= fft(x);
Y = fft(y);
disp('DFT of x[n] :'); disp(X); %displaying the value of X(k)
disp('DFT of y[n] :'); disp(Y); %displaying the value of Y(K)
subplot(6,1,3);
plot(X); %plot the DFT X(k)
xlabel('k'); ylabel('X');
title('X(k)');
subplot(6,1,4);
plot(Y); %plot the DFT Y(k)
xlabel('k'); ylabel('Y');
title('Y(k)');
Z = X.*Y;
disp('Product of the DFTs Z:'); disp(Z); %displaying the value of product Z(k) = X(k)*Y(k)
subplot(6,1,5);
plot(Z); %plot the dft of linear convolution Z(k)
xlabel('k'); ylabel('Z');
title('Z(k)');
z = ifft(Z); %Finding inverse of Z(k)
disp('Linear convolution of x[n] and y[n] :'); disp(z); %displaying the value of linear convolution z[n]
subplot(6,1,6);
plot(z); %plot the linear convolution z[n]
xlabel('n'); ylabel('z');
title('Linear convolution z[n]');
end
