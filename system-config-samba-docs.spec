Summary:	Documentation for configuring a Samba server
Name:		system-config-samba-docs
Version:	1.0.9
Release:	10
License:	GPLv2+
Group:		Books/Howtos
URL:		https://fedorahosted.org/%{name}
Source0:	http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	rarian
BuildRequires:	docbook-dtd45-xml

# Until version 1.2.67, system-config-samba contained online documentation.
# From version 1.2.68 on, online documentation is split off into its own
# package system-config-samba-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes:	system-config-samba < 1.2.68
Requires:	system-config-samba >= 1.2.68
Requires:	yelp
Requires:	rarian
BuildArch:	noarch


%description
This package contains the online documentation for system-config-samba which is
a graphical user interface for creating, modifying, and deleting samba shares.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%doc COPYING
%doc %{_datadir}/omf/system-config-samba
%doc %{_datadir}/gnome/help/system-config-samba


%changelog
* Fri May 27 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 680369
- initial realease
- imported package system-config-samba-docs

