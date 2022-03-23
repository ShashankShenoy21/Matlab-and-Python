
% Matlab code to generate a smiley face plot
t=0:0.001:2*pi;
x=2*cos(t);
y=1+2*sin(t);
fill(x,y,'o');
axis square
hold on
x2=-1+0.1*cos(t);
y2=2+0.1*sin(t);
fill(x2,y2,'k');
hold on;
x3=1+0.1*cos(t);
y3=2+0.1*sin(t);
fill(x3,y3,'k')
t=-0.4:0.1:0.4;
y=t.^2;
plot(t,y,'r','linewidth',15)