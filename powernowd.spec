Summary:		Daemon to adjust speed of your laptop processor
Name:			powernowd
Version:		0.97
Release:		%mkrel 2
License:		GPL
Group:			System/Servers
Source0:		http://www.deater.net/john/%{name}-%{version}.tar.bz2
Source1:		powernowd.rc.bz2
Source2:		powernowd.8.bz2
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
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -m755 %{name} $RPM_BUILD_ROOT/%{_sbindir}

bzcat %{SOURCE2} >%{name}.8
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m644 powernowd.8 $RPM_BUILD_ROOT/%{_mandir}/man8

mkdir -p $RPM_BUILD_ROOT/%{_initrddir}/
bzcat %{SOURCE1} > powernowd.rc
install -m755 powernowd.rc $RPM_BUILD_ROOT/%{_initrddir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/
install -m644 powernowd.sysconfig $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/%{name}


%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/*
%{_mandir}/man8/*
%config(noreplace) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}


