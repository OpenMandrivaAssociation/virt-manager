%define debug_package	%nil
%define	name	virt-manager
%define	version	0.9.4
%define	release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Manager
License:    GPLv2+
Group:      Graphical desktop/GNOME
URL:        http://virt-manager.org/
Source0:    http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Source1: state_paused.png
Source2: state_running.png
Source3: state_shutoff.png
BuildRequires:  python
BuildRequires:  pygtk2.0-devel
BuildRequires:  desktop-file-utils
BuildRequires:  scrollkeeper
BuildRequires:	intltool
Requires:       python-libvirt
Requires:       python-virtinst > 0.500.5
Requires:       python-vte
Requires:	    python-libxml2
Requires:	    python-gtk-vnc
Requires:	    dbus-python
Requires:	    pygtk2.0-libglade
Requires:	    gnome-python
Requires:	    gnome-python-gconf
Requires:	    gnome-python-gnomevfs
Requires:	    librsvg
Requires:	    libvirt-utils
Requires(post): GConf2
Requires(preun):GConf2

%description
The "Virtual Machine Manager" (virt-manager for short package name) is a
desktop application for managing virtual machines. It presents a summary view
of running domains and their live performance & resource utilization
statistics. A detailed view presents graphs showing performance & utilization
over time. Ultimately it will allow creation of new domains, and configuration
& adjustment of a domain's resource allocation & virtual hardware. Finally an
embedded VNC client viewer presents a full graphical console to the guest
domain.

%prep
%setup -q
cp %{SOURCE1} pixmaps
cp %{SOURCE2} pixmaps
cp %{SOURCE3} pixmaps

%build
%configure2_5x --with-qemu-user=qemu
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# menu entry
desktop-file-install --vendor="" \
    --add-category="GTK;GNOME;Emulator" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/virt-manager.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*
%{_libdir}/virt-manager-launch
%{_datadir}/virt-manager
%{_datadir}/applications/virt-manager.desktop
%{_datadir}/dbus-1/services/virt-manager.service
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_sysconfdir}/gconf/schemas/*
%{_mandir}/man1/*


%changelog
* Wed Jul 11 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.9.3-1
+ Revision: 808838
- version update 0.9.3

* Sun Oct 23 2011 Sergey Zhemoitel <serg@mandriva.org> 0.9.0-1
+ Revision: 705803
- add new version 0.9.0

  + Zé <ze@mandriva.org>
    - fix python-virtinst require (needs version 0.500.6)

* Mon Mar 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.7-1
+ Revision: 648673
- update to new version 0.8.7

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.6-1
+ Revision: 635799
- new version
- drop qemu perms patch: a configure switch is now available
- drop python patch: merged upstream

* Wed Nov 10 2010 Christiaan Welvaart <spturtle@mandriva.org> 0.8.5-2mdv2011.0
+ Revision: 595692
- Patch2: fix segfault with python 2.7

* Sun Sep 05 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.5-1mdv2011.0
+ Revision: 576171
- new version

* Sun Mar 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.4-1mdv2010.1
+ Revision: 528614
- update to new version 0.8.4

* Tue Feb 09 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.3-1mdv2010.1
+ Revision: 503314
- update to new version 0.8.3

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-1mdv2010.1
+ Revision: 478830
- new version

* Sat Oct 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-3mdv2010.0
+ Revision: 456539
- Disable Fedora patch which breaks VM creation when there is no
  user qemu

* Wed Oct 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-2mdv2010.0
+ Revision: 455735
- Sync patches with Fedora

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.0
+ Revision: 404172
- BuildRequires: intltool
- Update to new version 0.8.0
- Remove upstream patches

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-3mdv2010.0
+ Revision: 378311
- Add upstream patches, via Fedora:
  * Use openAuth when duplicating a connection when deleting a VM
  * Fix some OK/Cancel button ordering issues (RH bug #490207)
  * Fix incorrect max vcpu setting in New VM wizard (RH bug #490466)
  * Updated translations (RH bug 493795)
- Add Debian patches:
  * Use /usr/share/gconf for schema data
  * Close nc connection on EOF (Debian bugs #519979, #521137)
  * Don't crop VNC display (Debian bug #519979)
  * Fix keymap field in "Add hardware wizard" (Debian bug #528447)

* Mon Mar 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-2mdv2009.1
+ Revision: 362718
- Add 2 upstream bug fixes (via Fedora)

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-1mdv2009.1
+ Revision: 353929
- update to new version 0.7.0

* Wed Jan 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 334881
- update to new version 0.6.1

* Sat Dec 27 2008 Michael Scherer <misc@mandriva.org> 0.6.0-2mdv2009.1
+ Revision: 319891
- rebuild for new python

* Mon Oct 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1mdv2009.1
+ Revision: 293120
- new version
- drop keyboard patch (seems unneeded now)

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.5.4-2mdv2009.0
+ Revision: 269665
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4-1mdv2009.0
+ Revision: 194206
- update to new version 0.5.4

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-1mdv2008.1
+ Revision: 154206
- update to new version 0.5.3

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.5.2-2mdv2008.1
+ Revision: 106493
- rebuild for new lzma

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2-1mdv2008.1
+ Revision: 105238
- new version

* Thu Sep 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-5mdv2008.0
+ Revision: 93273
- patch1: make parsing /etc/sysconfig/keyboard a bit more robust

* Mon Sep 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-4mdv2008.0
+ Revision: 89236
- requires python-virtinst >= 0.300.0

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-3mdv2008.0
+ Revision: 85901
- add dependency on libvirt-utils

* Mon Sep 10 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-2mdv2008.0
+ Revision: 84244
- fix dependencies (fix #33395)

* Thu Aug 30 2007 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 75168
- add missing manpage
- New version 0.5.0

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.4.0-3mdv2008.0
+ Revision: 36212
- rebuild with correct optflags

* Mon Jun 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-2mdv2008.0
+ Revision: 35220
- fix dependencies (thanks Ze)

* Sat Jun 02 2007 Andreas Hasenack <andreas@mandriva.com> 0.4.0-1mdv2008.0
+ Revision: 34724
- updated to version 0.4.0

* Fri Apr 20 2007 Emmanuel Andry <eandry@mandriva.org> 0.3.1-3mdv2008.0
+ Revision: 15943
- fix missing requires (bug #30234)

