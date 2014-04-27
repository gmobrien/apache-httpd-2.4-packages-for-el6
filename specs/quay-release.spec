Summary:    quay.net yum repository configuration
Name:       quay-release
Version:    6
Release:    1%{?dist}
License:    GPLv2
Group:      System Environment/Base
URL:        https://bitbucket.org/ooburai
Source0:    quay.repo
Source1:    RPM-GPG-KEY-QUAY
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}
Requires:   yum

%description
This package contains yum configuration for the Quay RPM Repository,
as well as the public GPG key used to sign them.

%prep
echo empty prep

%build
echo empty build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -Dp -m0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/quay.repo
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-QUAY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/quay.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-QUAY

%changelog
* Sun Apr 27 2014 Gabriel O'Brien <gabriel.quay.net> - 6-1
- Initial release

