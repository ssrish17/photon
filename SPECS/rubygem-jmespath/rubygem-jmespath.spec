%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name jmespath

Name: rubygem-jmespath
Version:        1.6.2
Release:        2%{?dist}
Summary:        Implements JMESPath for Ruby.
Group:          Development/Languages
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}

Source0:        https://rubygems.org/downloads/jmespath-%{version}.gem
%define sha512 %{gem_name}=cd95094b00d7b9650d8811e9b7eefe15fcf0286c7a9bd1a7a40eae31a45ec1fb2b86b29901e03200a27743997694eee79fa463de2762044ca76d51f1fa3bd56e

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel

Requires: ruby

%description
Implements JMESPath for Ruby.

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
*   Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.6.2-2
-   Build gems properly
*   Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.6.2-1
-   Update to version 1.6.2
*   Wed Aug 17 2022 Gerrit Photon <photon-checkins@vmware.com> 1.6.1-1
-   Automatic Version Bump
*   Wed Sep 02 2020 Sujay G <gsujay@vmware.com> 1.4.0-2
-   rebuilt with ruby-2.7.1
*   Mon Jul 30 2018 Srinidhi Rao <srinidhir@vmware.com> 1.4.0-1
-   Initial build
