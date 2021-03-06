Summary: A collection of extra Java tools for the Binary Analysis Tool
Name: bat-extratools-java
Version: 27.0
Release: 1
License: BSD, public domain
Source: %{name}-%{version}.tar.gz
Group: Development/Tools
Packager: Armijn Hemel <armijn@binaryanalysis.org>
BuildRequires: ant, java-devel, jpackage-utils
Requires: java, jpackage-utils

%global debug_package %{nil}

%description
A collection of extra Java tools for the Binary Analysis Tool.

%prep
%setup -q
%build
ant
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dedexer/bat-ddx.jar $RPM_BUILD_ROOT%{_javadir}/bat-ddx.jar
%files
%{_javadir}/bat-ddx.jar
