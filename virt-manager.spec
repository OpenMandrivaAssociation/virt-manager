%define	name	virt-manager
%define	version	0.8.7
%define	release	%mkrel 1

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
%{_mandir}/man1/*
