Summary:		Daemon to adjust speed of your laptop processor
Name:			powernowd
Version:		1.00
Release:		9
License:		GPLv2 
Group:			System/Servers
Source0:		http://www.deater.net/john/%{name}-%{version}.tar.bz2
Source1:		powernowd.rc
Source2:		powernowd.8
URL:			http://www.deater.net/john/%{name}.html
ExclusiveArch:		%{ix86} ia64 x86_64 amd64 ppc
Requires(pre):		rpm-helper

%define debug_package %{nil}

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
mkdir -p %{buildroot}/%{_sbindir}
install -m755 %{name} %{buildroot}/%{_sbindir}

mkdir -p %{buildroot}/%{_mandir}/man8
install -m644 %{SOURCE2} %{buildroot}/%{_mandir}/man8

mkdir -p %{buildroot}/%{_initrddir}/
install -m755 %{SOURCE1} %{buildroot}/%{_initrddir}/%{name}

mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig/
install -m644 powernowd.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}


%post
%_post_service %{name}

%preun
%_preun_service %{name}

%files
%doc README
%attr(700,root,root) %{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/*
%{_mandir}/man8/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.00-6mdv2011.0
+ Revision: 667813
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.00-5mdv2011.0
+ Revision: 607199
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.00-4mdv2010.1
+ Revision: 523705
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.00-3mdv2010.0
+ Revision: 426775
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.00-2mdv2009.0
+ Revision: 225028
- rebuild

* Tue Jan 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.00-1mdv2008.1
+ Revision: 159936
- update to the latest version 1.00 (Frederik Himpe)
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 17 2007 Olivier Blin <oblin@mandriva.com> 0.97-3mdv2008.0
+ Revision: 53012
- add LSB tags in initscript (#28332)
- bunzip2 sources


* Mon Dec 18 2006 Olivier Blin <oblin@mandriva.com> 0.97-2mdv2007.0
+ Revision: 98654
- do not require cpufreq, frequency scaling modules are now configured by DrakX/harddrake
- Import powernowd

* Fri Mar 10 2006 Jerome Soyer <saispo@mandriva.org> 0.97-1mdk
- New release 0.97

* Thu May 19 2005 Danny Tholen <obiwan@mailmij.org> 0.96-2mdk
- add ppc to arches

* Sun May 15 2005 Michael Scherer <misc@mandriva.org> 0.96-1mdk
- New release 0.96
- fix prereq
- use mkrel

* Tue Mar 15 2005 Olivier Blin <oblin@mandrakesoft.com> 0.95-1mdk
- 0.95

* Sun Jan 30 2005 Michael Scherer <misc@mandrake.org> 0.90-5mdk 
- fix bug #13303, thanks to the reporter
- fix rpmlint error

* Wed Aug 25 2004 Erwan Velu <erwan@mandrakesoft.com> 0.90-4mdk 
- Requires cpufreq

* Sun Jun 06 2004 Michael Scherer <misc@mandrake.org> 0.90-3mdk 
- change description & summary

* Sun Jun 06 2004 Michael Scherer <misc@mandrake.org> 0.90-2mdk 
- update url ( thanks Adam Williamson )

* Sat Jun 05 2004 Michael Scherer <misc@mandrake.org> 0.90-1mdk
- some adjustement
- from Nicolas Brouard <nicolas.brouard@libertysurf.fr>
	- initial contribs version of powernowd package

