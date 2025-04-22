%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name webrick

Name:           rubygem-webrick
Version:        1.8.1
Release:        2%{?dist}
Summary:        HTTP server toolkit
Group:          Development/Languages
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}

Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=3bf45e3a52190dccaa6e883923448b745a420eff2a1533eacdd2aed0e4c67f5c6d813c85606f8fc12952c004e4984fd97ebc3c361a42b49cebe5b84c8fc6e99d

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel

Requires: ruby

BuildArch: noarch

%description
WEBrick is an HTTP server toolkit that can be configured as an HTTPS server,
a proxy server, and a virtual-host server.

%prep
%gem_unpack %{SOURCE0}

%build
%gem_build

%install
%gem_install

%files
%defattr(-,root,root,-)
%{gemdir}

%changelog
* Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.8.1-2
- Build gems properly
* Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.8.1-1
- Update to version 1.8.1
* Fri Oct 20 2023 Shreenidhi Shedi <sshedi@vmware.com> 1.7.0-1
- Initial version. Needed by rubygem-fluentd.
