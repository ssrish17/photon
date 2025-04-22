%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name multi_json

Name:           rubygem-multi_json
Version:        1.15.0
Release:        3%{?dist}
Summary:        Ruby Gem for JSON parsing and encoding
Group:          Development/Languages
Vendor:         VMware, Inc.
URL:            https://rubygems.org/gems/%{gem_name}
Distribution:   Photon

Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=5021b66bd607bde8679899ff48fbf596cdf6a4f6c026472b20f25bd1933d105bef597c143ab529804d7b5a4a244476be24555f13a7fbe9fef30bbe1fb92978eb

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel

Requires: ruby

%description
MultiJson is a library that provides a common interface to several JSON implementation libraries in Ruby.

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
* Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.15.0-3
- Build gems properly
* Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.15.0-2
- Bump Version to build with new ruby
* Fri Oct 20 2023 Shreenidhi Shedi <sshedi@vmware.com> 1.15.0-1
- Initial version.
- Needed by rubygem-fluent-plugin-kubernetes_metadata_filter.
