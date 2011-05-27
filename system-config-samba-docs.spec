Summary: Documentation for configuring a Samba server
Name: system-config-samba-docs
Version: 1.0.9
Release: %mkrel 1
URL: https://fedorahosted.org/%{name}
License: GPLv2+
Group: Documentation
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%__id_u -n)
BuildArch: noarch
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: rarian

# Until version 1.2.67, system-config-samba contained online documentation.
# From version 1.2.68 on, online documentation is split off into its own
# package system-config-samba-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-samba < 1.2.68
Requires: system-config-samba >= 1.2.68
Requires: yelp
Requires: rarian

%description
This package contains the online documentation for system-config-samba which is
a graphical user interface for creating, modifying, and deleting samba shares.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-samba
%doc %{_datadir}/gnome/help/system-config-samba
