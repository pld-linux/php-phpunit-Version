%define		status		stable
%define		pearname	Version
%include	/usr/lib/rpm/macros.php
Summary:	Library that helps with managing the version number of Git-hosted PHP projects
Name:		php-phpunit-Version
Version:	1.0.1
Release:	1
License:	The BSD 3-Clause License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	2f946dfc4e1c84d676a46c9364c81825
URL:		http://pear.phpunit.de/package/Version/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library that helps with managing the version number of Git-hosted PHP
projects

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Version/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/SebastianBergmann
%{php_pear_dir}/SebastianBergmann/Version
