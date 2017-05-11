Name:		virt-manager
Version:	1.4.1
Release:	1
Summary:	Virtual Machine Manager
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://virt-manager.org/
Source0:	http://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	python
BuildRequires:	intltool
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildArch: noarch
Requires:	python2-libvirt
Requires:	python2-libxml2
Requires:	python-urlgrabber
Requires:	python2-gi
Requires:	libvirt-glib
Requires:	python-ipaddr
Requires:	typelib(Gtk) = 3.0
Requires:	typelib(GtkVnc) = 2.0
Requires:	typelib(SpiceClientGtk) = 3.0
Requires:	typelib(Vte) = 2.91
Requires:	typelib(LibvirtGLib)
Obsoletes:	python-virtinst < 0.600.5

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

%build
%{__python2} ./setup.py configure --prefix=%{_prefix} \
	--libvirt-package-names="libvirt-utils" \
	--kvm-package-names="qemu" \
	--askpass-package-names="openssh-askpass" \
	--stable-defaults \
	--preferred-distros="OpenMandriva"
%{__python2} ./setup.py build

%install
%{__python2} ./setup.py \
	--no-update-icon-cache --no-compile-schemas \
	 install --root=%{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/virt-manager.appdata.xml
%{_datadir}/GConf/gsettings/org.virt-manager.virt-manager.convert
%{_mandir}/man*/*
%{_iconsdir}/*/*/*/*
%{_datadir}/%{name}
