%global debug_package %{nil}
%global gemdir %(IFS=: R=($(gem env gempath)); echo ${R[${#R[@]}-1]})
%global gem_name http-cookie

Name: rubygem-http-cookie
Version:        1.0.5
Release:        3%{?dist}
Summary:        HTTP::Cookie is a Ruby library to handle HTTP Cookies based on RFC 6265.
Group:          Development/Libraries
Vendor:         VMware, Inc.
Distribution:   Photon
URL:            https://rubygems.org/gems/%{gem_name}/versions/%{version}

Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
%define sha512 %{gem_name}=d530d64b5c2fc3757a6de03384fe768317e24a523d4a4215f5bcc6b5bca9e7b94eeaad1e52fbb67548396b7b2ca7c9d8b68ea7b99109e24770fcf34c950469ef

BuildRequires: ruby-devel

Source1: license.txt
%include %{SOURCE1}

BuildRequires: ruby-devel
BuildRequires: rubygem-domain_name

Requires: rubygem-domain_name >= 0.5.0, rubygem-domain_name < 1.0.0
Requires: ruby

BuildArch: noarch

%description
HTTP::Cookie is a Ruby library to handle HTTP Cookies based on RFC 6265. It has with
security, standards compliance and compatibility in mind, to behave just the same as
today's major web browsers. It has builtin support for the legacy cookies.txt and the
latest cookies.sqlite formats of Mozilla Firefox, and its modular API makes it easy
to add support for a new backend store.

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
* Thu Apr 17 2025 Shreenidhi Shedi <shreenidhi.shedi@broadcom.com> 1.0.5-3
- Build gems properly
* Mon Feb 26 2024 Shivani Agarwal <shivani.agarwal@broadcom.com> 1.0.5-2
- Bump Version to build with new ruby
*   Wed Aug 17 2022 Gerrit Photon <photon-checkins@vmware.com> 1.0.5-1
-   Automatic Version Bump
*   Wed Sep 02 2020 Sujay G <gsujay@vmware.com> 1.0.3-2
-   Rebuilt using ruby-2.7.1
*   Thu Aug 22 2019 Stanislav Hadjiiski <hadjiiskis@vmware.com> 1.0.3-1
-   Initial build
