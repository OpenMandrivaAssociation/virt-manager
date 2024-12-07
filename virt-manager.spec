# Please keep this package in sync with FC

%global __requires_exclude typelib\\\(AppIndicator3\\\)|typelib\\\(Vte\\\) = 2.90

# RPM doesn't detect that code in /usr/share is python3, this forces it
# https://fedoraproject.org/wiki/Changes/Avoid_usr_bin_python_in_RPM_Build#Python_bytecompilation
%global __python %{__python3}

Name: virt-manager
Version:	5.0.0
Release:	1
%global verrel %{version}-%{release}
Summary: Desktop tool for managing virtual machines via libvirt
Group: Graphical desktop/GNOME
License: GPLv2+
BuildArch: noarch
URL: https://virt-manager.org/
Source0: https://virt-manager.org/download/sources/%{name}/%{name}-%{version}.tar.xz

Requires: virt-manager-common = %{verrel}
Requires: python-gobject3
Requires: python-ipaddr
Requires: python-libvirt
Requires: python-requests
Requires: python-gi-cairo
Requires: typelib(Gtk) = 3.0
Requires: typelib(GtkVnc) = 2.0
Requires: typelib(SpiceClientGtk) = 3.0
Requires: typelib(GtkSource)
Requires: %{_lib}gtksourceview-gir4
Requires: %{_lib}vte-gir2.91
Requires: spice-gtk
# virt-manager works fine with either, so pull the latest bits so there's
# no ambiguity.
Requires: typelib(Vte) >= 2.91
Requires: typelib(libxml2)
Requires: libvirt-utils
# Dirty fix for bug https://issues.openmandriva.org/show_bug.cgi?id=2677
Requires: %{_lib}virt-glib-gir1.0
Requires: %{_lib}osinfo-gir1.0
Requires: osinfo-db
Requires: qemu-audio-spice

BuildRequires: meson
BuildRequires: intltool
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: python-docutils

%description
Virtual Machine Manager provides a graphical tool for administering virtual
machines for KVM, Xen, and LXC. Start, stop, add or remove virtual devices,
connect to a graphical or serial console, and see resource usage statistics
for existing VMs on local or remote machines. Uses libvirt as the backend
management API.

%package common
Summary: Common files used by the different Virtual Machine Manager interfaces
Group:    Emulators

Requires: python-libvirt
Requires: python-libxml2
Requires: python-requests
Requires: python-ipaddr
# Required for gobject-introspection infrastructure
Requires: python-gobject3
# Required for pulling files from iso media with isoinfo
Requires: genisoimage
Conflicts: virt-manager < 1.3.2-5

%description common
Common files used by the different virt-manager interfaces, as well as
virt-install related tools.


%package -n virt-install
Summary: Utilities for installing virtual machines
Group:    Emulators
Requires: virt-manager-common = %{verrel}
# For 'virsh console'
Requires: libvirt-utils
Requires: %{_lib}osinfo1.0_0

Provides: virt-install
Provides: virt-clone
Provides: virt-convert
Provides: virt-xml
Conflicts: virt-manager < 1.3.2-5

%description -n virt-install
Package includes several command line utilities, including virt-install
(build and install new VMs) and virt-clone (clone an existing virtual
machine).

# Fix --initrd-inject with f30 URLs (bz #1686464)
%patch0001 -p1
%patch0002 -p1


%prep
%setup -q
%autopatch -p1

%build
	
%meson \
     -Ddefault-hvs="qemu,xen,lxc" \
     -Dupdate-icon-cache=false \
     -Dcompile-schemas=false \
     -Dtests=disabled
     
%meson_build

%install
%meson_install

	
%find_lang %{name}

%files
%doc README.md COPYING NEWS.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/%{name}/virtManager
%{_datadir}/%{name}/icons
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.virt-manager.virt-manager.gschema.xml
%{_datadir}/metainfo/%{name}.appdata.xml

%files common -f %{name}.lang
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/virtinst

%files -n virt-install
%{_mandir}/man1/virt-install.1*
%{_mandir}/man1/virt-clone.1*
%{_mandir}/man1/virt-xml.1*
%{_datadir}/bash-completion/completions/virt-install
%{_datadir}/bash-completion/completions/virt-clone
%{_datadir}/bash-completion/completions/virt-xml
%{_bindir}/virt-install
%{_bindir}/virt-clone
%{_bindir}/virt-xml
