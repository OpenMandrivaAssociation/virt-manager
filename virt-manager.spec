%define	name	virt-manager
%define	version	0.7.0
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Virtual Machine Manager
License:    GPLv2+
Group:      Graphical desktop/GNOME
URL:        http://virt-manager.org/
Source:     http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
# Upstream patches, via Fedora
Patch1: %{name}-%{version}-old-xen-compat.patch
Patch2: %{name}-%{version}-vm-migrate-list.patch
Patch3: %{name}-%{version}-fix-button-ordering.patch
Patch4: %{name}-%{version}-fix-vcpu-cap.patch
Patch5: %{name}-%{version}-delete-dup-conn.patch
Patch6: %{name}-%{version}-update-translations.patch
# Upstream patches, via Debian
Patch101:	0001-use-usr-share-gconf-for-schema-data.patch
Patch102:	0002-close-nc-connection-on-EOF.patch
Patch103:	0003-don-t-crop-vnc-display.patch
Patch104:	0004-make-check-match-return-value-of-self.get_config_key.patch
BuildRequires:  python
BuildRequires:  pygtk2.0-devel
BuildRequires:  desktop-file-utils
BuildRequires:  scrollkeeper
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

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
%{_libdir}/virt-manager
%{_libdir}/virt-manager-launch
%{_datadir}/virt-manager
%{_datadir}/applications/virt-manager.desktop
%{_datadir}/dbus-1/services/virt-manager.service
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/gnome/help/virt-manager/
%{_datadir}/omf/virt-manager/
%{_mandir}/man1/*
