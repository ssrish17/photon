%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name mustache

Name: rubygem-mustache
Version:        1.1.1
Release:        4%{?dist}
Summary:        A framework-agnostic way to render logic-free views
Group:          Development/Languages
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}
Vendor:         VMware, Inc.
Distribution:   Photon

Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=91a18a374a0348317d0801d6784fedd0782d7a08f128d3ab7050e631b34e45cecd49c4b1e2a9e17204f70bf169c107a92a1e210532bd3faa98edf8b1b5e8e43c

Source1: license.txt
%include %{SOURCE1}

BuildRequires:  ruby-devel

Requires: ruby

%description
Mustache is a replacement for your views. Instead of views consisting of
ERB or HAML with random helpers and arbitrary logic, your views are broken
into two parts: a Ruby class and an HTML template

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
*   Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.1.1-4
-   Build gems properly
*   Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.1.1-3
-   Bump Version to build with new ruby
*   Thu Dec 08 2022 Shivani Agarwal <shivania2@vmware.com> 1.1.1-2
-   Bump version to build with new Ruby
*   Thu Sep 17 2020 Him Kalyan Bordoloi <bordoloih@vmware.com> 1.1.1-1
-   Initial build
