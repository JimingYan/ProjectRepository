MyCurrent=table2array(Current); %change the name of the table if your .csv file is named differently 
time=MyCurrent(:,1);
phase1=MyCurrent(:,2);
phase2=MyCurrent(:,3);
phase3=MyCurrent(:,4);

figure(1);
plot(time,phase1);
grid on;
hold on;

%%Uncomment for phase2
%plot(time,phase2)

%%Uncomment for phase3
%plot(time,phase3)

figure(2);
timeseg=time(2)-time(1);
Fs=1/timeseg;
f=0:Fs/length(time):(Fs*(1-1/length(time)));
f=f-Fs/2;
phaseFFT1=fftshift(fft(phase1))/length(time);
plot(f(1000:1999),abs((phaseFFT1(1000:1999))));
grid on;
hold on;

%%Uncomment for phase2
%phaseFFT2=fftshift(fft(phase2))/length(time);
%plot(f(1000:1999),abs((phaseFFT2(1000:1999))));
%hold on;

%%Uncomment for phase3
%phaseFFT3=fftshift(fft(phase3))/length(time);
%plot(f(1000:1999),abs((phaseFFT3(1000:1999))));
%hold on;

