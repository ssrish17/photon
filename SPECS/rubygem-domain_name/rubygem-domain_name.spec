%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name domain_name

Name: rubygem-domain_name
Version:        0.6.20240107
Release:        2%{?dist}
Summary:        This is a Domain Name manipulation library for Ruby.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}

Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=9911389bdfdae984f697726cd7feff5a41b944a98982cfa76d49002c4f64e51d0ec7db6259eddc97fecbcc13c9723134af26b83e050c31943dc8495866874d59

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel
BuildRequires: rubygem-unf

Requires: rubygem-unf >= 0.0.5, rubygem-unf < 1.0.0
Requires: ruby

BuildArch: noarch

%description
This is a Domain Name manipulation library for Ruby. It can also be used for
cookie domain validation based on the Public Suffix List.

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
*   Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 0.6.20240107-2
-   Build gems properly
*   Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 0.6.20240107-1
-   Update to version 0.6.20240107
*   Wed Sep 02 2020 Sujay G <gsujay@vmware.com> 0.5.20190701-2
-   Rebuilt using ruby-2.7.1
*   Thu Aug 22 2019 Stanislav Hadjiiski <hadjiiskis@vmware.com> 0.5.20190701-1
-   Initial build
