%define	name	virt-manager
%define	version	0.8.0
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Manager
License:    GPLv2+
Group:      Graphical desktop/GNOME
URL:        http://virt-manager.org/
Source:     http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
Source1: state_paused.png
Source2: state_running.png
Source3: state_shutoff.png
# Fix disk XML mangling via connect/eject cdrom (RH bug #516116)
Patch1: %{name}-%{version}-cdrom-eject-driver.patch
# Fix delete button sensitivity (RH bug #518536)
Patch2: %{name}-%{version}-no-delete-active.patch
# Fix populating text box from storage browser in 'New VM' (RH bug #517263)
Patch3: %{name}-%{version}-newvm-storage-cb.patch
# Fix a traceback in an 'Add Hardware' error path (RH bug #517286)
Patch4: %{name}-%{version}-addhw-errmsg-typo.patch
# Fixes for pylint script to return nicer results on F11/F12
Patch5: %{name}-%{version}-pylint-tweak.patch
# Don't close libvirt connection for non-fatal errors (RH bug #522168)
Patch6: %{name}-%{version}-conn-close-exception.patch
# Manager UI tweaks
Patch7: %{name}-%{version}-manager-ui-tweaks.patch
# Generate better errors is disk/net stats polling fails
Patch8: %{name}-%{version}-stats-logging.patch
# Refresh host disk space in create wizard (RH bug #502777)
Patch9: %{name}-%{version}-refresh-disk-space.patch
# Offer to fix disk permission issues (RH bug #517379)
Patch10: %{name}-%{version}-fix-path-perms.patch
# Fix VCPU hotplug
Patch11: %{name}-%{version}-fix-vcpu-hotplug.patch
# Remove access to outdated docs (RH bug #522823, bug #524805)
Patch12: %{name}-%{version}-hide-help-docs.patch
# Update VM state text in manager view (RH bug #526182)
Patch13: %{name}-%{version}-update-vm-state.patch
# Update translations (RH bug #493795)
Patch14: %{name}-%{version}-update-translations.patch
# More translations (RH bug #493795)
Patch15: %{name}-%{version}-more-translations.patch
# Don't allow creating a volume without a name (RH bug #526111)
Patch16: %{name}-%{version}-createvol-name.patch
# Don't allow volume allocation > capacity (RH bug #526077)
Patch17: %{name}-%{version}-createvol-alloc.patch
# Add tooltips for toolbar buttons (RH bug #524083)
Patch18: %{name}-%{version}-toolbar-tooltips.patch
BuildRequires:  python
BuildRequires:  pygtk2.0-devel
BuildRequires:  desktop-file-utils
BuildRequires:  scrollkeeper
BuildRequires:	intltool
Requires:       python-libvirt
Requires:       python-virtinst >= 0.300.0
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
BuildRoot:           %{_tmppath}/%{name}-%{version}

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
%configure2_5x
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

%clean
rm -rf %{buildroot}


%if %mdkversion < 200900
%post
%post_install_gconf_schemas virt-manager
%{update_menus}
%endif

%preun
%preun_uninstall_gconf_schemas virt-manager

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%{_bindir}/*
%{_libdir}/virt-manager-launch
%{_datadir}/virt-manager
%{_datadir}/applications/virt-manager.desktop
%{_datadir}/dbus-1/services/virt-manager.service
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/gnome/help/virt-manager/
%{_datadir}/omf/virt-manager/
%{_mandir}/man1/*
