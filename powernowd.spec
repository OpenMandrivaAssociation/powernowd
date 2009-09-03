Summary:		Daemon to adjust speed of your laptop processor
Name:			powernowd
Version:		1.00
Release:		%mkrel 3
License:		GPLv2 
Group:			System/Servers
Source0:		http://www.deater.net/john/%{name}-%{version}.tar.bz2
Source1:		powernowd.rc
Source2:		powernowd.8
URL:			http://www.deater.net/john/%{name}.html
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:		%{ix86} ia64 x86_64 amd64 ppc
Requires(pre):		rpm-helper

%description
This is a very simple daemon that will adjust the speed of your 
CPU depending on system load.

It only works with a supported processor found on some laptops, 
with the cpufreq interface.

%prep 
%setup -q

%build
%make

%install
cat > powernowd.sysconfig <<EOF
# place here the option passed to powernowd.
# They are described in powernowd(8)
#
#   -n   Include 'nice'd processes in calculations
#   -m   Modes of operation, can be 0, 1, 2, or 3:
#          0 = SINE, 1 = AGGRESSIVE (default), 2 = PASSIVE, 3 = LEAPS
#   -s   Frequency step in kHz (default = 100000)
#   -p   Polling frequency in msecs (default = 1000)
#   -u   CPU usage upper limit percentage [0 .. 100, default 80]
#   -l   CPU usage lower limit percentage [0 .. 100, default 20]
#

OPTIONS=""

EOF
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_sbindir}
install -m755 %{name} %{buildroot}/%{_sbindir}

mkdir -p %{buildroot}/%{_mandir}/man8
install -m644 %{SOURCE2} %{buildroot}/%{_mandir}/man8

mkdir -p %{buildroot}/%{_initrddir}/
install -m755 %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/
install -m644 powernowd.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}


%clean
rm -rf %{buildroot}

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%doc README
%attr(700,root,root) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/*
%{_mandir}/man8/*
